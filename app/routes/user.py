from fastapi import APIRouter, Depends,HTTPException,status#(the staus helps to understand the status of the error and the exception calls ou the error)
from database import SessionLocal
from sqlalchemy.orm import Session
from db_models import User
from pd_models import UserIn,UserOut,UserUpdateIn
from passlib.context import CryptContext #importing a cryptography context
from uuid import UUID






user_route = APIRouter(tags=["Users Route"]) 

#function to retrieve database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() #Always close database

#creating a password context variable
pass_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

#creting a new item into the backend
@user_route.post("/create_user",response_model=UserOut)
async def create_new_user(user:UserIn,db:Session = Depends(get_db)):
    #let us hash the password first
    hashed_password = pass_context.hash(user.password)
    new_user = User(email = user.email, firstname = user.firstname,lastname = user.lastname,password = hashed_password,phonenumber=user.phonenumber)
    db.add(new_user) #telling sqlalchemy to add this to database
    db.commit() #this saves new changes in database
    db.refresh(new_user) #this updates user objects
    return new_user




#Get something from backend
@user_route.get("/get_user_by_id",response_model=UserOut) # this is the endpoint
async def get_user_by_id(id:UUID,db:Session=Depends(get_db)):
    user = db.query(User).filter(User.id==id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="there is no exixsting user with the provided id"
        )
       
    return user




#Update items in backend
@user_route.put("/update_phonenumber",response_model=UserOut)
async def update_phone_number(user:UserUpdateIn,db:Session=Depends(get_db)):
    db_user = db.query(User).filter(User.id == user.id).first()
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = "User is not found.Enter the correct ID. "
        )
    elif db_user.phonenumber == user.phoneNumber:
        raise HTTPException(
           status_code=status.HTTP_400_BAD_REQUEST,
           detail = "Phone numberis the same. It should be different." 
        )
    elif user.phoneNumber is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Please provide a phone number."
        )
        
    
    db_user.phonenumber = user.phonenumber
    db.commit()
    db.refresh(db_user)
    return db_user


@user_route.put("/update_firstname",response_model=UserOut)
async def update_first_name(user:UserUpdateIn,db:Session=Depends(get_db)):
    db_user = db.query(User).filter(User.id == user.id).first()
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = "User is not found. "
        )

    db_user.firstname = user.firstname
    db.commit()
    db.refresh(db_user)
    return db_user









#deleting items in backend
@user_route.delete("/delete_user")
async def delete_user(id:UUID,db:Session=Depends(get_db)):
    db_user = db.query(User).filter(User.id == id).first()
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The id does not match an existing user."
        )
    db.delete(db_user)
    db.commit()
    return db_user






