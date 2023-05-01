from pydantic import BaseModel
from datetime import datetime

class TokenData(BaseModel):
	id: str | None = None