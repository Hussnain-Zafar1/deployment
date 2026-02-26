from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="Health Check API", version="1.0.0")


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to Health Check API",
        "status": "running"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "Health Check API"
    }


@app.get("/api/v1/status")
async def detailed_status():
    """Detailed status endpoint"""
    return {
        "status": "operational",
        "uptime": "running",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0"
    }
