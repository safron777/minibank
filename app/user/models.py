from sqlalchemy import Column, Identity, Integer, String, ForeignKey,ForeignKeyConstraint, Sequence, FLOAT 
from app.database import Base
from typing import TYPE_CHECKING
#from app.account.models import User_accounts
from sqlalchemy.orm import relationship, mapped_column, Mapped

if TYPE_CHECKING:
    # Убирает предупреждения отсутствия импорта и неприятные подчеркивания в 
    # PyCharm и VSCode
    from account.models import User_accounts


class Users(Base):
    __tablename__="users"
    #id = Column(Integer, Sequence('users_id_seq', start=1), primary_key=True)
    #username=Column(String,primary_key=True,nullable=False, unique=True)
    #email = Column (String, nullable=False, primary_key=True, unique=True)
    #firstname = Column(String,nullable=False)
    #lastname = Column (String, nullable=False)
    #surname = Column (String, nullable=False)
    #password= Column (String,nullable=True)
    #ForeignKeyConstraint (['users.email'],['users_accounts.username_acc'],use_alter=True, name= 'fk_email_username_acc')
    #email= relationship(back_populates="user_accounts")
    #hashed_password = Column(String,nullable=False)
   # __table_args__ = (ForeignKeyConstraint([username],[User_accounts.username]), {})
    
    id: Mapped[int] = mapped_column(Integer, Identity(start=1, always=True),primary_key=True, unique=True)
    email: Mapped[str]= mapped_column(String,unique=True)
    firstname: Mapped[str]= mapped_column(nullable=False)
    lastname: Mapped [str] = mapped_column(nullable=False)
    surname: Mapped [str] = mapped_column(nullable=False)
    password: Mapped [str] = mapped_column(nullable=False)

   # user_accounts: Mapped[list["User_accounts"]] = relationship(back_populates="username_acc")
    

