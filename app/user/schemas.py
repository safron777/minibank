from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional

from pydantic import BaseModel

class SUsers(BaseModel):
    #id: int
    #username : str
    email: EmailStr 
    firstname :str 
    lastname : str
    surname : str
    #password: str
    password:str
   
    model_config = ConfigDict(from_attributes=True)



class SUserAuth(BaseModel):
    
    email: EmailStr
    password: str

    model_config = ConfigDict(from_attributes=True)