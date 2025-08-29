import json
import requests
from typing import Dict, Any, Optional
from .config import Config

class AIClient:
    def __init__(self):
        self.config = Config()
        self.conversation_history = []
        
    def add_to_history(self, role: str, content: str):
        """Add message to conversation history"""
        self.conversation_history.append({"role": role, "content": content})
    
    def get_system_prompt(self) -> str:
        """Read system prompt from file"""
        try:
            with open(self.config.SYSTEM_PROMPT_FILE, 'r', encoding='utf-8') as f:
                return f.read().strip()
        except FileNotFoundError:
            return "You are a helpful AI assistant."
    
    def call_openai(self, user_message: str) -> Optional[str]:
        """Make API call to OpenAI"""
        if not self.config.OPENAI_API_KEY:
            return None
            
        headers = {
            "Authorization": f"Bearer {self.config.OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }
        
        messages = [
            {"role": "system", "content": self.get_system_prompt()}
        ] + self.conversation_history + [
            {"role": "user", "content": user_message}
        ]
        
        data = {
            "model": self.config.OPENAI_MODEL,
            "messages": messages,
            "temperature": 0.7
        }
        
        try:
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=30
            )
            response.raise_for_status()
            result = response.json()
            return result["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"OpenAI API error: {e}")
            return None
    
    def call_ollama(self, user_message: str) -> Optional[str]:
        """Make API call to Ollama"""
        messages = [
            {"role": "system", "content": self.get_system_prompt()}
        ] + self.conversation_history + [
            {"role": "user", "content": user_message}
        ]
        
        data = {
            "model": self.config.OLLAMA_MODEL,
            "messages": messages,
            "stream": False
        }
        
        try:
            response = requests.post(
                f"{self.config.OLLAMA_BASE_URL}/api/chat",
                json=data,
                timeout=30
            )
            response.raise_for_status()
            result = response.json()
            return result["message"]["content"]
        except Exception as e:
            print(f"Ollama API error: {e}")
            return None
    
    def get_response(self, user_message: str) -> Optional[str]:
        """Get AI response using available API"""
        # Add user message to history
        self.add_to_history("user", user_message)
        
        # Try OpenAI first (unless explicitly set to use Ollama)
        if not self.config.USE_OLLAMA:
            response = self.call_openai(user_message)
            if response:
                self.add_to_history("assistant", response)
                return response
        
        # Fallback to Ollama
        response = self.call_ollama(user_message)
        if response:
            self.add_to_history("assistant", response)
            return response
        
        return "Sorry, I couldn't get a response from any AI service."
    
    def reset_conversation(self):
        """Reset conversation history"""
        self.conversation_history = []
