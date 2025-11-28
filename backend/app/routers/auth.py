from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from app.database import SessionLocal
from app.models import User
from app.schemas import UserSchema, UserCreateSchema
from app.utils import get_db
from app.auth import authenticate_user, create_access_token

router = APIRouter(prefix='/api/v1/auth', tags=['auth'])

@router.post('/register')
def register(user: UserCreateSchema, db: SessionLocal = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user is not None:
        return JSONResponse(content={'error': 'Username already taken'}, media_type='application/json', status_code=400)
    new_user = User(username=user.username, email=user.email, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return JSONResponse(content={'token': create_access_token(new_user.id), 'user_id': new_user.id}, media_type='application/json', status_code=201)

@router.post('/login')
def login(user: UserCreateSchema, db: SessionLocal = Depends(get_db)):
    user = authenticate_user(user.username, user.password, db)
    if user is None:
        return JSONResponse(content={'error': 'Invalid username or password'}, media_type='application/json', status_code=401)
    return JSONResponse(content={'token': create_access_token(user.id), 'user_id': user.id}, media_type='application/json')
