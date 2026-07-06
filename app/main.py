from fastapi import FastAPI, Request, UploadFile, File
from pathlib import Path
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()
BASE_DIR = Path(__file__).parent


recording_dir = BASE_DIR / "recordings"
os.makedirs(recording_dir, exist_ok=True)


templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")


@app.get("/")
async def record(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
    )


@app.post("/upload")
async def upload(audio: UploadFile = File(...)):
    filepath = recording_dir / audio.filename

    with open(filepath, "wb") as f:
        f.write(await audio.read())

    return {"message": "saved"}
