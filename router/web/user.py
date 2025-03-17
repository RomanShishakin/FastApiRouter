from fastapi import APIRouter
from fastapi.responses import HTMLResponse

user = APIRouter()


@user.get("/v1/user")
def read_root():
    html_content = "<h2>web/v1/user</h2>"
    return HTMLResponse(content=html_content)