from datetime import date
from fastapi.background import P
from sqlalchemy import Column, Integer, String, ForeignKey, ForeignKeyConstraint,VARCHAR, FLOAT, Computed
from sqlalchemy.orm import Mapped, mapped_column,relationship
from typing import TYPE_CHECKING

from app.database import Base
from app.users import models
from app.users.models import Users

if TYPE_CHECKING:
    # Убирает предупреждения отсутствия импорта и неприятные подчеркивания в 
    # PyCharm и VSCode
    from account.models import User_accounts

class User_accounts(Base):
   __tablename__="user_accounts"
  

   id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
   
  
   accounts: Mapped[str]= mapped_column(nullable=False)
   balance: Mapped [float] = mapped_column(nullable=False)
   interest_rate: Mapped [float]=mapped_column(nullable=True)
   data_time: Mapped[date]= mapped_column(nullable=False)
   
   username_acc: Mapped[str]
  