from models import customer
from fastapi import APIRouter
import random

router = APIRouter(prefix="/Orders")

@router.get("/{id}")
async def getOrders(id):
    orders = customer.readOrders(id)
    return orders
    