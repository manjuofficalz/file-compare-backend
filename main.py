from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Initialize the FastAPI app
app = FastAPI(
    title="File Compare Platform Backend",
    description="API for managing files, users, and comparisons.",
    version="0.1.0",
)

# Configure CORS
origins = [
    "http://localhost",
    "http://localhost:5173",  # Vite's default development server port
    "http://localhost:3000",  # Docker frontend container
    "http://frontend:3000",   # Docker service name
    # Add your Vercel frontend domain here once deployed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the File Compare Platform API!"}

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "backend-api"}

# Placeholder for future API endpoints (e.g., /auth, /files, /admin)
# from .routers import auth, files, admin
# app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
# app.include_router(files.router, prefix="/files", tags=["Files"])
# app.include_router(admin.router, prefix="/admin", tags=["Admin"])
