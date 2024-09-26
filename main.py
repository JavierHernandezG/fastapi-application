from fastapi import FastAPI
import logging

app = FastAPI()

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
)

logger = logging.getLogger(__name__)

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == '__main__':
    import uvicorn

    print("Hello (⌐■_■)")
    uvicorn.run("main:app", port=8000, reload=True, log_level="info")
