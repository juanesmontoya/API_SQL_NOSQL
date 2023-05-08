from controllers import controller_sqlite as sqlite
from controllers import controlller_sqlserver as sqlserver
from controllers import controller_mix as orders
from fastapi import FastAPI, APIRouter
import random

#start server with python -m uvicorn main:app --reload

app = FastAPI()

app.include_router(sqlserver.router)
app.include_router(sqlite.router)
app.include_router(orders.router)

@app.get("/")
async def root():
    return "Aqui va la app principal"

