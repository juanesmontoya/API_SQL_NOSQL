from models import inventario
from fastapi import APIRouter
import json

router = APIRouter(prefix="/Gaseosas")

@router.get("/{name}")
async def getGaseosasQuantity(name):
    gaseosas = inventario.readGaseosaCantidad(name)
    return gaseosas

@router.get("/")
async def getNames():
    gaseosa = inventario.readGaseosa()
    jsongaseosas = [tuple(row) for row in gaseosa]
    json_string = json.dumps(jsongaseosas)
    return json_string

@router.post("/")
async def setGaseosa(name,brand,quantity):
    try:
        inventario.insertGaseosa(name,brand,quantity)
        return "Gaseosa created Sucessfully."
    except:
        return "Gaseosa not created."
    
@router.put("/")
async def updateGaseosa(name,quantity):
    newQuantity = int(quantity)-1
    try:
        inventario.updateGaseosa(name,newQuantity)
        return "Quantity updated."
    except:
        return "Something went wrong."

@router.delete("/")
async def deleteGaseosa(name):
    try:
        inventario.deleteGaseosa(name)
        return "Gaseosa deleted."
    except:
        return "Something went wrong."