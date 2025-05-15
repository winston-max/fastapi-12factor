from fastapi import FastAPI
from app.config import settings
from app.routes import health

app = FastAPI(title=settings.APP_NAME, docs_url="/docs")

app.include_router(health.router)

@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.APP_NAME}!"}