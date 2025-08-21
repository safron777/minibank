from sqlalchemy import Column, Integer, String, ForeignKey, ForeignKeyConstraint, BOOLEAN

from app.database import Base
#from app.users import models
#from app.users.models import Users

class feature_toggle(Base):
    __tablename__="feature_toggle"
    id = Column(Integer,primary_key=True)
    feature_toggle=Column(BOOLEAN,nullable=False)
    