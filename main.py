from controllers import controller_sqlite as sqlite
from controllers import controlller_sqlserver as sqlserver
from controllers import controller_mix as orders
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

#start server with python -m uvicorn main:app --reload
#create instance of fastapi
app = FastAPI()

#add static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

#add HTML views directory
templates = Jinja2Templates(directory="views")

#use instance to include routes/endpoints
app.include_router(sqlserver.router)
app.include_router(sqlite.router)
app.include_router(orders.router)

#create main rout for the project
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    text = "Nacional Campeon de AMERICA 2016"
    return templates.TemplateResponse("main.html",{"request":request, "text":text})

