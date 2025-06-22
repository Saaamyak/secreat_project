from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from .routes import ask

app = FastAPI()
app.include_router(ask.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type", "Authorization"]
)

@app.get("/", tags=["Root"])
async def read_root():
  return { 
    "message": "Welcome to API backend",
   }

@app.get("/health")
async def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
  uvicorn.run("main:app", host="0.0.0.0", port=8000)
