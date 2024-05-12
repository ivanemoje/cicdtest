from fastapi import FastAPI
from home import home
from api import api

app = FastAPI()

app.include_router(home)
app.include_router(api)
