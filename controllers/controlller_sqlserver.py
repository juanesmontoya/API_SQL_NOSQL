#Import models for data transfer. Fastapi for API purposes and json librarie to clean data from end to end.
from models import customer
from fastapi import APIRouter
import json

#set router for API route Customer
router = APIRouter(prefix="/Customer")

#HTTP get petition of all Customers
@router.get("/")
async def getCustomers():
    customers = customer.readCustomers()
    jsoncustomers = [tuple(row) for row in customers]
    json_string = json.dumps(jsoncustomers)
    return json_string

#HTTP get petition of one Customer
@router.get("/{id}")
async def getCustomer(id):
    oneCustomer = customer.readCustomer(id)
    jsonCustomer = [tuple(row) for row in oneCustomer]
    json_string = json.dumps(jsonCustomer)
    return json_string

#HTTP post petition to create customer
@router.post("/")
async def setCustomer(name,phone):
    try:
        customer.insertCustomer(name,phone)
        return "Customer created Sucessfully."
    except:
        return "Customer not created."

#HTTP put petition to modify a customer
@router.put("/")
async def updateCustomer(id,name, phone):
    try:
        customer.updateCustomer(id,name, phone)
        return "Customer updated."
    except:
        return "Something went wrong"

#HTTP delete petition to delete a customer
@router.delete("/")
async def deleteCustomer(id):
    try:
        customer.deleteCustomer(id)
        return "Customer deleted."
    except:
        return "Something went wrong"