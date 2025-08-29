const API_BASE_URL = 'http://localhost:8000';

export interface ChatRequest {
  message: string;
  model?: 'auto' | 'openai' | 'ollama';
  reset_conversation?: boolean;
}

export interface ChatResponse {
  response: string;
  conversation_id?: string;
  model_used?: string;
}

export interface ConversationResetResponse {
  message: string;
  success: boolean;
}

export const api = {
  async chat(request: ChatRequest): Promise<ChatResponse> {
    const response = await fetch(`${API_BASE_URL}/api/ideation/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(request),
    });
    
    if (!response.ok) {
      throw new Error(`API error: ${response.status}`);
    }
    
    return response.json();
  },

  async resetConversation(): Promise<ConversationResetResponse> {
    const response = await fetch(`${API_BASE_URL}/api/ideation/reset`, {
      method: 'POST',
    });
    
    if (!response.ok) {
      throw new Error(`API error: ${response.status}`);
    }
    
    return response.json();
  },

  async getConfig() {
    const response = await fetch(`${API_BASE_URL}/api/ideation/config`);
    
    if (!response.ok) {
      throw new Error(`API error: ${response.status}`);
    }
    
    return response.json();
  }
};
