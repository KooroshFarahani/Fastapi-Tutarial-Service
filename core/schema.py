from pydantic import BaseModel
from typing import Optional


class UserBase (BaseModel):
    id:int
    name:str
    age:int

class UserCreate(UserBase):
    id:int

class UserUpdate(BaseModel):
    name: Optional [str]=None
    age : Optional[int]=None

class user (UserBase):
    id:int
