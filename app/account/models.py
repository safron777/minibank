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
   #id= Column(Integer,primary_key=True, nullable=False)
   #username_acc=Column(ForeignKey("users.email"))
   #accounts = Column (Integer, nullable=False)
   #balance= Column (FLOAT,nullable=False)
   #interest_rate= Column (FLOAT, nullable=False)
  # ForeignKeyConstraint (['users.email'],['users_accounts.username_acc'],use_alter=True, name= 'fk_email_username_acc')
   #ForeignKeyConstraint(['Table1ID'], ['Table1.ID'], name='fk_Table2_Table1')

   id: Mapped[int] = mapped_column(primary_key=True,unique=True)
   
   #username_acc: Mapped[str]= mapped_column(ForeignKey("users.email"),primary_key=True, unique=True)
   accounts: Mapped[str]= mapped_column(nullable=False)
   balance: Mapped [float] = mapped_column(nullable=False)
   interest_rate: Mapped [float]=mapped_column(nullable=True)
   data_time: Mapped[date]= mapped_column(nullable=False)
   #data_time: Mapped[date]= mapped_column()
   username_acc: Mapped[str]= mapped_column(ForeignKey("users.email"),primary_key=True, unique=True)
   username_acc: Mapped["Users"] = relationship(back_populates="user_accounts")