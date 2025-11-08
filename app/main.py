from fastapi import FastAPI#(the staus helps to understand the status of the error and the exception calls ou the error)
from database import engine
from db_models import Base
from routes import user,transactions



try:
    Base.metadata.create_all(bind=engine)
    print("tables created")
except Exception as e:
    print("errors creating table: ",e)

myapp = FastAPI() 

# including routes here:
myapp.include_router(user.user_route)
myapp.include_router(transactions.transaction_route)
