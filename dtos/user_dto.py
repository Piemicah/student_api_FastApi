from typing import Optional

from pydantic import BaseModel


class UserResponse(BaseModel):
    id:int
    username:str
    role_id:int
    model_config = {"from_attributes": True}

class UserCreate(BaseModel):
    username:str
    password:str
    role_id:int

class UserUpdate(BaseModel):
    username:Optional[str]=None
    role_id:Optional[int]=None