from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from kink import di

from db.current_session import current_session
from src.container.container import init_container
from src.places.controller import router as places_router

app = FastAPI()
app.include_router(places_router)
templates = Jinja2Templates(directory="static")


@app.on_event("startup")
async def startup_event():
    init_container()


@app.get("/page/{page_name}", response_class=HTMLResponse)
async def root(request: Request, page_name: str):
    data = {"page": page_name}
    return templates.TemplateResponse("page.html", {"request": request, "data": data})


@app.middleware("http")
async def local_session(request, call_next):
    async with di["session_maker"]() as session:
        current_session.set(session)
        response = await call_next(request)
    return response