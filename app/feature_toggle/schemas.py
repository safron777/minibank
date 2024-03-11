from pydantic import BaseModel, ConfigDict

class SAccounts(BaseModel):
    id: int 
    feature_toggle: bool
   
    model_config = ConfigDict(from_attributes=True)