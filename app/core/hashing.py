from datetime import datetime, timedelta
from typing import Any, Union

from jose import jwt
from passlib.context import CryptContext

import os 
from dotenv import load_dotenv

load_dotenv()


ALGORITHM = os.getenv('ALGORITHM')

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")




def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)