from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger)
    last_name = Column('last_name', String)
    first_name = Column('first_name', String)
    registrate_date = Column('registrate_date', DateTime(), default=datetime.now)


class ActionsUsers(Base):
    __tablename__ = 'actions_users'

    id = Column(Integer, primary_key=True)
    user_id = ForeignKey("users.id")
    date = Column('date', DateTime(), default=datetime.now)
