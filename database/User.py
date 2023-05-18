from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker, subqueryload
from sqlalchemy import Table, event
from __init__ import engine, session, Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255))
    address_id = Column(Integer, ForeignKey('address.id'))
    address = relationship('Address', backref='address_user', cascade='all, delete')

    def __repr__(self):
        return f'<User(id={self.id}, name={self.name}, email={self.email}, address={self.address})'
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}