from fastapi import APIRouter

transaction_route = APIRouter(tags=["Transactions Route"])

@transaction_route.get("/get_transaction")
async def get_transaction():
    return{"message": "Transaction obtained. "}
