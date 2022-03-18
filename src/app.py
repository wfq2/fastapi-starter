from fastapi import FastAPI

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from src.places.controller import router as places_router
from src.container.container import init_container

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
