from fastapi import FastAPI, HTTPException
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from kink import di

from container.request_context import RequestContext
from exceptions.does_not_exist_exception import DoesNotExistException
from src.container.container import init_container
from src.places.controller import router as places_router
from src.users.controller import router as user_router
from users.models.user import anonymous_user
from users.security_service import SecurityService

app = FastAPI()
app.include_router(places_router)
app.include_router(user_router)
templates = Jinja2Templates(directory="static")


@app.on_event("startup")
async def startup_event():
    init_container()


@app.get("/page/{page_name}", response_class=HTMLResponse)
async def root(request: Request, page_name: str):
    data = {"page": page_name}
    return templates.TemplateResponse("page.html", {"request": request, "data": data})


@app.middleware("http")
async def set_user_if_exists(request: Request, call_next):
    service = di[SecurityService]
    try:
        user = await service.get_user_from_request(request)
        RequestContext.set_request_user(user)
    except (HTTPException, DoesNotExistException):
        RequestContext.set_request_user(anonymous_user)
    response = await call_next(request)
    return response


@app.middleware("http")
async def local_db_session(request: Request, call_next):
    async with di["session_maker"]() as session:
        RequestContext.set_request_session(session)
        response = await call_next(request)
    return response
