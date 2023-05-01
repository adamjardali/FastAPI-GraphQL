from sqlalchemy import Column, Integer, DateTime, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship 
from datetime import datetime

from db.database import Base 

var_length = 100




class User(Base):
	__tablename__ = 'Users'
	id = Column(Integer,primary_key = True, index = True)
	name = Column(String(var_length),nullable = False, default = "New User")
	email = Column(String(var_length), nullable = False, unique = True)
	password = Column(String(var_length), nullable = False)
	created_at = Column(DateTime, nullable  = False, default = datetime.utcnow)
	image = Column(String(var_length),default = "new_user.png", nullable = False)
	date_of_birth = Column(DateTime, default = datetime.utcnow, nullable = False)
	country = Column(String(var_length), nullable = False, default = "Lebanon")
	is_active = Column(Boolean,nullable = False, default = True)
	is_superuser = Column(Boolean, nullable = False, default = False)
	# posts = relationship('Task', back_populates = 'creator')