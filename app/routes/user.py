from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import utils, schema
from ..models import User
from fastapi import HTTPException, status

router = APIRouter(
    prefix="/users",
    tags=['users']
)

@router.post("/", response_model=schema.UserOut)
def create_user(user: schema.User, db: Session = Depends(get_db)):
    hashed_password = utils.generate_hash(user.password)
    # Create a SQLAlchemy User instance instead of Pydantic
    new_user = User(
        name=user.name,
        email=user.email,
        password=hashed_password
    )
    
    ## Check if the user with email id already exhists
    user = db.query(User).filter(User.email == user.email).first()
    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/{user_id}", response_model=schema.UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)): 
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.get("/", response_model=list[schema.UserOut])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users
