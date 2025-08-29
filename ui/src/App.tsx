import { IdeationProvider } from '@/contexts/IdeationContext';
import { ChatInterface } from '@/components/ChatInterface';

function App() {
  return (
    <IdeationProvider>
      <div className="min-h-screen bg-background">
        <ChatInterface />
      </div>
    </IdeationProvider>
  );
}

export default App;
