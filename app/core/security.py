from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os



from db import database
from models.user import User
from schemas.token import TokenData

load_dotenv()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
ACCESS_TOKEN_EXPIRE_MINUTES = 30

get_db = database.get_db

def create_access_token(data: dict):
	
	to_encode = data.copy()
	expire_time = datetime.utcnow() + timedelta(minutes = int(ACCESS_TOKEN_EXPIRE_MINUTES))
	to_encode.update({'exp':expire_time})
	token  = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)
	return token

def verify_access_token(token: str, credentials_exception):

    try:

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data = TokenData(id=id)
    except JWTError:
        raise credentials_exception

    return token_data


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail=f"Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})

    token = verify_access_token(token, credentials_exception)

    user = db.query(User).filter(User.id == token.id).first()

    return user