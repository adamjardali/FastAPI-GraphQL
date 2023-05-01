from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, DateTime, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship 
from datetime import datetime

from db.database import Base 

if TYPE_CHECKING:
	from .user import User
	

class Friendship(Base):
	__tablename__ = "Friends"
	friend_request = Column(Integer, ForeignKey('Users.id',ondelete = "CASCADE"), primary_key = True)	
	friend_accept = Column(Integer, ForeignKey('Users.id',ondelete = "CASCADE"), primary_key = True)	
	created_at = Column(DateTime, nullable = False, default = datetime.utcnow)
