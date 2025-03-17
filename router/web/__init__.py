from .token import token
from .user import user

def web_routers():
    return [token, user]