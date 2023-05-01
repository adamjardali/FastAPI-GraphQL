from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, DateTime, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship 
from datetime import datetime

from db.database import Base 

if TYPE_CHECKING:
	from .user import User



class Post(Base):
    __tablename__ = "Posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    content = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())