from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from .ai_client import AIClient

router = APIRouter(prefix="/api/ideation", tags=["ideation"])

# Initialize AI client
ai_client = AIClient()

# Pydantic models for request/response
class ChatRequest(BaseModel):
    message: str = Field(..., description="User message for AI ideation")
    model: Optional[str] = Field("auto", description="AI model to use: auto, openai, or ollama")
    reset_conversation: Optional[bool] = Field(False, description="Reset conversation history")

class ChatResponse(BaseModel):
    response: str = Field(..., description="AI response")
    conversation_id: Optional[str] = Field(None, description="Conversation identifier")
    model_used: Optional[str] = Field(None, description="Model used for response")

class ConversationResetResponse(BaseModel):
    message: str = Field(..., description="Reset confirmation message")
    success: bool = Field(..., description="Reset operation success status")

@router.post("/chat", response_model=ChatResponse, summary="Chat with AI Ideation Assistant")
async def chat(request: ChatRequest):
    """
    Chat with the AI ideation assistant for product development guidance.
    
    - **message**: Your product idea or question
    - **model**: Choose AI model (auto, openai, ollama)
    - **reset_conversation**: Reset chat history if needed
    """
    try:
        # Handle conversation reset if requested
        if request.reset_conversation:
            ai_client.reset_conversation()
            return ChatResponse(
                response="Conversation history has been reset. How can I help you with your product ideation?",
                conversation_id="reset",
                model_used="auto"
            )
        
        # Set model preference
        if request.model == "ollama":
            ai_client.config.USE_OLLAMA = True
            model_used = "ollama"
        elif request.model == "openai":
            ai_client.config.USE_OLLAMA = False
            model_used = "openai"
        else:
            model_used = "auto"
        
        # Get AI response
        response = ai_client.get_response(request.message)
        
        if not response:
            raise HTTPException(status_code=500, detail="Failed to get AI response")
        
        return ChatResponse(
            response=response,
            conversation_id="current_session",
            model_used=model_used
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing chat request: {str(e)}")

@router.post("/reset", response_model=ConversationResetResponse, summary="Reset Conversation")
async def reset_conversation():
    """
    Reset the current conversation history to start fresh.
    """
    try:
        ai_client.reset_conversation()
        return ConversationResetResponse(
            message="Conversation history has been reset successfully",
            success=True
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error resetting conversation: {str(e)}")

@router.get("/history", summary="Get Conversation History")
async def get_conversation_history():
    """
    Retrieve the current conversation history and message count.
    """
    try:
        return {
            "conversation_history": ai_client.conversation_history,
            "total_messages": len(ai_client.conversation_history)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving conversation history: {str(e)}")

@router.get("/config", summary="Get Configuration")
async def get_config():
    """
    Get current API configuration and available models.
    """
    try:
        return {
            "openai_available": bool(ai_client.config.OPENAI_API_KEY),
            "ollama_available": True,  # Assuming Ollama is always available locally
            "current_model": "ollama" if ai_client.config.USE_OLLAMA else "openai",
            "openai_model": ai_client.config.OPENAI_MODEL,
            "ollama_model": ai_client.config.OLLAMA_MODEL
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving configuration: {str(e)}")
