from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker, subqueryload
from sqlalchemy import Table, event
from __init__ import engine, session, Base

class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    street = Column(String(255), nullable=False)
    number = Column(Integer)

    def __repr__(self):
        return f'<Address(id={self.id}, street={self.street}, number={self.number})'
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}