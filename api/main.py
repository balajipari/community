from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from ideation.routes import router as ideation_router

# Initialize FastAPI app with Swagger docs
app = FastAPI(
    title="Product Community API",
    description="API for product ideation and community features",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include ideation routes
app.include_router(ideation_router)

# Health check endpoint
@app.get("/")
async def root():
    return {"message": "Product Community API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "Product Community API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
