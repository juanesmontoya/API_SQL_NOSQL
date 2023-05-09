from models import customer
from fastapi import APIRouter
import random

router = APIRouter(prefix="/Orders")

@router.get("/{OrderNumber}")
async def getOrders(OrderNumber):
    orders = customer.readOrders(OrderNumber)
    return orders
    