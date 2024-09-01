from sqlalchemy import *
from extention import db, get_current_time

class Email(db.Model, UserMixin):
    __tablename__ = "emails"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False, index=True)
    date_create = Column(String(12), default=get_current_time)