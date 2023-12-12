import uvicorn

from src.config import get_settings

settings = get_settings()

if __name__ == "__main__":
    uvicorn.run(settings.app, host=settings.host, port=settings.port)
