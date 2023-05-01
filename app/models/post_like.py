from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, DateTime, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship 
from datetime import datetime

from db.database import Base 

if TYPE_CHECKING:
	from .user import User
	from .post import Post

class Post_Like(Base):
	__tablename__ = "Posts_Likes"
	id = Column(Integer, primary_key = True, index = True)
	post_id = Column(Integer, ForeignKey('Posts.id',ondelete = "CASCADE"))	
	user_id = Column(Integer, ForeignKey('Users.id',ondelete = "CASCADE"))
	created_at = Column(DateTime, nullable = False, default = datetime.utcnow)
