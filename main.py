from fastapi import FastAPI
import logging
from fastapi_application.settings import Settings

settings = Settings()
app = FastAPI(title=settings.app_name)

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
)
#hola

logger = logging.getLogger(__name__)

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == '__main__':
    import uvicorn

    print("Hello (⌐■_■)")
    uvicorn.run("main:app", port=8000, reload=True, log_level="info")
