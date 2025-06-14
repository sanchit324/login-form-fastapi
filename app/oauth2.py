from jose import JWTError, jwt
from .config import settings
from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from .schema import TokenData
from .models import User    
from .database import get_db
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login/")

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
TOKEN_EXPIRATION_TIME = settings.TOKEN_EXPIRATION_TIME

## create access token
def create_access_token(data: dict):
    to_encode = data.copy()
    to_encode.update({"exp": datetime.now(timezone.utc) + timedelta(minutes=60)})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str, credentials_exception):
    try: 
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        id: str = payload.get("user_id")    
        if id is None:
            raise credentials_exception
        token_data = TokenData(id=id)
    except JWTError:
        raise credentials_exception
    return token_data
    
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> TokenData:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data = verify_access_token(token, credentials_exception)
    user = db.query(User).filter(User.id == token_data.id).first()
    return user