import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')
    
    # Ollama Configuration (for local models)
    OLLAMA_BASE_URL = os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434')
    OLLAMA_MODEL = os.getenv('OLLAMA_MODEL', 'llama2')
    
    # Default to OpenAI if available, otherwise Ollama
    USE_OLLAMA = os.getenv('USE_OLLAMA', 'false').lower() == 'true'
    
    # System prompt file
    SYSTEM_PROMPT_FILE = 'system_prompt.txt'
