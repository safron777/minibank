from pydantic import BaseModel,ConfigDict
from typing import Optional
from datetime import date

class SAccounts(BaseModel):
   id: int
   username_acc: str
   accounts: int
   balance: float
   interest_rate: float
   
   
   model_config = ConfigDict(from_attributes=True)
""""
class SNewAccount(BaseModel):
    id: int

    date_from: date
    date_to: date
    """






class SAccounts_balance(BaseModel):
   #id:int
   #username_acc: str
   #accounts: int
   balance: float
   interest_rate: float
   model_config = ConfigDict(from_attributes=True)

class SAccounts_interest_rate(BaseModel):
   interest_rate: float
   model_config = ConfigDict(from_attributes=True)
