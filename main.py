from fastapi import FastAPI
from router.api import api_routers
from router.web import web_routers
 
app = FastAPI()
 

for router in api_routers():
     app.include_router(router, prefix="/api")

for router in web_routers():
     app.include_router(router, prefix="/web")