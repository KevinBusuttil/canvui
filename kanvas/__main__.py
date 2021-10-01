# __main__.py
from .app import kanvas 
import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from pathlib import Path

app = FastAPI()        

base_path = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(base_path / "templates"))
app.mount("/static", StaticFiles(directory=str(base_path / "static")), name="static")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("app.html", {"request": request})

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)    
    kanvas = kanvas()
    if kanvas:
        kanvas.run()
    