import { createContext, useContext, useReducer, type ReactNode } from 'react';

interface Message {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  timestamp: Date;
}

interface IdeationState {
  messages: Message[];
  isLoading: boolean;
  error: string | null;
}

type IdeationAction =
  | { type: 'ADD_MESSAGE'; payload: Message }
  | { type: 'SET_LOADING'; payload: boolean }
  | { type: 'SET_ERROR'; payload: string | null }
  | { type: 'RESET_CONVERSATION' };

const initialState: IdeationState = {
  messages: [],
  isLoading: false,
  error: null,
};

function ideationReducer(state: IdeationState, action: IdeationAction): IdeationState {
  switch (action.type) {
    case 'ADD_MESSAGE':
      return {
        ...state,
        messages: [...state.messages, action.payload],
        error: null,
      };
    case 'SET_LOADING':
      return {
        ...state,
        isLoading: action.payload,
      };
    case 'SET_ERROR':
      return {
        ...state,
        error: action.payload,
        isLoading: false,
      };
    case 'RESET_CONVERSATION':
      return {
        ...state,
        messages: [],
        error: null,
      };
    default:
      return state;
  }
}

interface IdeationContextType {
  state: IdeationState;
  addMessage: (role: 'user' | 'assistant', content: string) => void;
  setLoading: (loading: boolean) => void;
  setError: (error: string | null) => void;
  resetConversation: () => void;
}

const IdeationContext = createContext<IdeationContextType | undefined>(undefined);

export function IdeationProvider({ children }: { children: ReactNode }) {
  const [state, dispatch] = useReducer(ideationReducer, initialState);

  const addMessage = (role: 'user' | 'assistant', content: string) => {
    const message: Message = {
      id: Date.now().toString(),
      role,
      content,
      timestamp: new Date(),
    };
    dispatch({ type: 'ADD_MESSAGE', payload: message });
  };

  const setLoading = (loading: boolean) => {
    dispatch({ type: 'SET_LOADING', payload: loading });
  };

  const setError = (error: string | null) => {
    dispatch({ type: 'SET_ERROR', payload: error });
  };

  const resetConversation = () => {
    dispatch({ type: 'RESET_CONVERSATION' });
  };

  const value: IdeationContextType = {
    state,
    addMessage,
    setLoading,
    setError,
    resetConversation,
  };

  return (
    <IdeationContext.Provider value={value}>
      {children}
    </IdeationContext.Provider>
  );
}

export function useIdeation() {
  const context = useContext(IdeationContext);
  if (context === undefined) {
    throw new Error('useIdeation must be used within an IdeationProvider');
  }
  return context;
}
