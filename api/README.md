# Ideation Buddy CLI

A CLI-based AI chat system designed to guide founders through the product ideation phase. The system uses structured prompts to capture essential product information step-by-step.

## Features

- 🤖 AI-powered ideation guidance
- 📋 Structured interview process
- 🔄 Support for both OpenAI and Ollama models
- 💾 Conversation history tracking
- 🎨 Rich terminal interface
- 📊 JSON-formatted responses for easy parsing

## Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd api
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   ```bash
   # Copy the example file
   cp env_example.txt .env
   
   # Edit .env with your API keys
   # For OpenAI:
   OPENAI_API_KEY=your_openai_api_key_here
   
   # For Ollama (optional):
   USE_OLLAMA=true
   OLLAMA_MODEL=llama2
   ```

## Usage

### Basic Usage
```bash
python cli.py
```

### Command Line Options
```bash
# Use specific AI model
python cli.py --model openai    # Use OpenAI
python cli.py --model ollama    # Use Ollama
python cli.py --model auto      # Auto-detect (default)

# Reset conversation history
python cli.py --reset

# Get help
python cli.py --help
```

### Example Session
```
🚀 Ideation Buddy CLI
Your AI-powered product ideation assistant

Starting ideation session...
Type 'quit' or 'exit' to end the session

You: I want to build a productivity app
AI Assistant: What best describes the motto/vision of your product?

You: 1
AI Assistant: What main problem are you solving?

You: People struggle to manage their time effectively
AI Assistant: Who do you imagine will use your product?
...
```

## Configuration

### OpenAI Setup
1. Get an API key from [OpenAI](https://platform.openai.com/)
2. Add to `.env`: `OPENAI_API_KEY=your_key_here`

### Ollama Setup (Local Models)
1. Install [Ollama](https://ollama.ai/)
2. Pull a model: `ollama pull llama2`
3. Set in `.env`: `USE_OLLAMA=true`

## System Prompt

The system uses a structured prompt from `system_prompt.txt` that guides the AI through:
1. **Motto/Vision** - Product purpose
2. **Problem Statement** - What problem you're solving
3. **Target Users** - Who will use it
4. **ICP** - Ideal Customer Profile
5. **Persona** - Detailed user persona
6. **Value Proposition** - Unique value
7. **Alternatives** - Current solutions

## Project Structure

```
api/
├── cli.py              # Main CLI interface
├── ai_client.py        # AI API client
├── config.py           # Configuration management
├── system_prompt.txt   # AI system prompt
├── requirements.txt    # Python dependencies
├── env_example.txt     # Environment variables example
└── README.md          # This file
```

## Development

This is an MVP implementation focusing on the ideation phase. The system:
- Maintains conversation context
- Provides structured guidance
- Returns JSON-formatted responses
- Supports multiple AI backends

## Troubleshooting

- **"No API key found"**: Check your `.env` file and API key
- **"Connection error"**: Verify Ollama is running locally
- **"Model not found"**: Ensure the specified model is available

## License

[Your License Here]
