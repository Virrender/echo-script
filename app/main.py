from fastapi import FastAPI
from .routes import recordings
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from .database import Base, engine


BASE_DIR = Path(__file__).parent

Base.metadata.create_all(engine)
app = FastAPI()
app.include_router(recordings.router)

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
