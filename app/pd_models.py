#pydantic model defines how data should come in and go out of the data base.
from pydantic import BaseModel,EmailStr
from uuid import UUID


class UserIn(BaseModel):
    firstname:str
    lastname:str
    email:EmailStr
    password:str
    phonenumber:str



class UserOut(BaseModel):
    firstname:str
    id:UUID
    email:EmailStr
    lastname:str
    phonenumber:str

#model for updates coming
class UserUpdateIn(BaseModel):
    id:UUID
    phonenumber:str=None
    firstname:str=None
    lastname:str=None