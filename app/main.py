from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# Create all tables defined in models.py (if they don't already exist)
from app.database import Base, engine
from app import models
Base.metadata.create_all(engine)



from app.config import BASE_DIR
from app.routes import recordings
from app.routes import auth

app = FastAPI()

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

app.include_router(recordings.router)
app.include_router(auth.router)


