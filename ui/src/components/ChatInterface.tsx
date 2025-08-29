import React, { useState } from 'react';
import { useIdeation } from '@/contexts/IdeationContext';
import { api } from '@/lib/api';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Send, RotateCcw, Bot, User } from 'lucide-react';

export function ChatInterface() {
  const { state, addMessage, setLoading, setError, resetConversation } = useIdeation();
  const [inputValue, setInputValue] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!inputValue.trim() || state.isLoading) return;

    const userMessage = inputValue.trim();
    setInputValue('');
    
    // Add user message
    addMessage('user', userMessage);
    setLoading(true);
    setError(null);

    try {
      const response = await api.chat({ message: userMessage });
      addMessage('assistant', response.response);
    } catch (error) {
      setError(error instanceof Error ? error.message : 'Failed to get response');
    } finally {
      setLoading(false);
    }
  };

  const handleReset = async () => {
    try {
      await api.resetConversation();
      resetConversation();
    } catch (error) {
      setError(error instanceof Error ? error.message : 'Failed to reset conversation');
    }
  };

  return (
    <div className="max-w-4xl mx-auto p-4 space-y-4">
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <Bot className="h-6 w-6" />
            Product Ideation Assistant
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            {/* Messages */}
            <div className="space-y-3 max-h-96 overflow-y-auto">
              {state.messages.length === 0 ? (
                <div className="text-center text-muted-foreground py-8">
                  Start your product ideation journey by asking a question!
                </div>
              ) : (
                state.messages.map((message) => (
                  <div
                    key={message.id}
                    className={`flex gap-3 ${
                      message.role === 'user' ? 'justify-end' : 'justify-start'
                    }`}
                  >
                    <div
                      className={`flex gap-2 max-w-[80%] ${
                        message.role === 'user' ? 'flex-row-reverse' : 'flex-row'
                      }`}
                    >
                      <div className="flex-shrink-0 w-8 h-8 rounded-full bg-primary flex items-center justify-center">
                        {message.role === 'user' ? (
                          <User className="h-4 w-4 text-primary-foreground" />
                        ) : (
                          <Bot className="h-4 w-4 text-primary-foreground" />
                        )}
                      </div>
                      <div
                        className={`rounded-lg px-3 py-2 ${
                          message.role === 'user'
                            ? 'bg-primary text-primary-foreground'
                            : 'bg-muted'
                        }`}
                      >
                        {message.content}
                      </div>
                    </div>
                  </div>
                ))
              )}
              {state.isLoading && (
                <div className="flex gap-3 justify-start">
                  <div className="flex gap-2">
                    <div className="flex-shrink-0 w-8 h-8 rounded-full bg-primary flex items-center justify-center">
                      <Bot className="h-4 w-4 text-primary-foreground" />
                    </div>
                    <div className="bg-muted rounded-lg px-3 py-2">
                      <div className="flex space-x-1">
                        <div className="w-2 h-2 bg-muted-foreground rounded-full animate-bounce"></div>
                        <div className="w-2 h-2 bg-muted-foreground rounded-full animate-bounce" style={{ animationDelay: '0.1s' }}></div>
                        <div className="w-2 h-2 bg-muted-foreground rounded-full animate-bounce" style={{ animationDelay: '0.2s' }}></div>
                      </div>
                    </div>
                  </div>
                </div>
              )}
            </div>

            {/* Error Display */}
            {state.error && (
              <div className="bg-destructive/10 border border-destructive/20 rounded-lg p-3 text-destructive text-sm">
                {state.error}
              </div>
            )}

            {/* Input Form */}
            <form onSubmit={handleSubmit} className="flex gap-2">
              <Input
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                placeholder="Describe your product idea..."
                disabled={state.isLoading}
                className="flex-1"
              />
              <Button type="submit" disabled={state.isLoading || !inputValue.trim()}>
                <Send className="h-4 w-4" />
              </Button>
              <Button
                type="button"
                variant="outline"
                onClick={handleReset}
                disabled={state.isLoading}
              >
                <RotateCcw className="h-4 w-4" />
              </Button>
            </form>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
