from fastapi import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends
from fastapi import HTTPException, status    
from sqlalchemy.orm import Session    
from ..database import get_db    
from ..models import User    
from ..oauth2 import create_access_token    
from .. import utils, schema

router = APIRouter(
    prefix="/auth",
    tags=['auth']
)

@router.post("/login", response_model=schema.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    password_hash = utils.verify_password(user_credentials.password, user.password)
    if not password_hash:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    access_token = create_access_token(data={"user_id": user.id})
    
    return schema.Token(
        access_token=access_token, 
        token_type="bearer"
    )