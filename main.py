from controllers import controller_sqlite as sqlite
from controllers import controlller_sqlserver as sqlserver
from controllers import controller_mix as orders
from fastapi import FastAPI, APIRouter
import random

#start server with python -m uvicorn main:app --reload
#create instance of fastapi
app = FastAPI()

#use instance to include routes/endpoints
app.include_router(sqlserver.router)
app.include_router(sqlite.router)
app.include_router(orders.router)

#create main rout for the project
@app.get("/")
async def root():
    return "Aqui va la app principal"

