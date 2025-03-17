from fastapi import APIRouter
from fastapi.responses import HTMLResponse

token = APIRouter(tags=['Работа с токеном'])


@token.get("/v1/token")
def read_root():
    html_content = "<h2>api/v1/token</h2>"
    return HTMLResponse(content=html_content)