from fastapi import APIRouter, Request, Form
from app.templates import templates
from sqlalchemy.orm import Session
from app.database import engine
from pwdlib import PasswordHash
password_hash=PasswordHash.recommended()


from app.models import Users

router=APIRouter()


@router.get("/signup")
async def users(request: Request):
    return templates.TemplateResponse(
            request=request,
            name="signup.html"
    )

@router.post("/signup")
async def signup(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):
    hashed_pswd=password_hash.hash(password)
    with Session(engine) as session:
        user= Users(
            username=username,
            hashed_password=hashed_pswd
        )
        session.add(user)
        session.commit()
    
    return {"message": "User created"}
    
    
