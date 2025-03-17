from fastapi import APIRouter
from fastapi.responses import HTMLResponse

token = APIRouter()


@token.get("/v1/token")
def read_root():
    html_content = "<h2>web/v1/token</h2>"
    return HTMLResponse(content=html_content)