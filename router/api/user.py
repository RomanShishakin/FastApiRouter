from fastapi import APIRouter
from fastapi.responses import HTMLResponse

user = APIRouter(tags=['Работа с пользователем'])


@user.get("/v1/user")
def read_root():
    html_content = "<h2>api/v1/user</h2>"
    return HTMLResponse(content=html_content)

@user.get("/v2/user")
def read_root():
    html_content = "<h2>api/v2/user</h2>"
    return HTMLResponse(content=html_content)