from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker, subqueryload
from sqlalchemy import Table, event
from __init__ import engine, session, Base
from Address import Address

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
    
class Queries():
    @staticmethod
    def add_user(**kwargs):
        try:
            with session:
                user = User()
                columns = [c.name for c in user.__table__.columns][1:]
                for col in columns:
                    if col in kwargs['user']:
                        setattr(user, col, kwargs['user'][col])
                adress = Address()
                columns_address = [c.name for c in adress.__table__.columns][1:]
                for col in columns_address:
                    if col in kwargs['address']:
                        setattr(user, col, kwargs['address'][col])
                user.address = adress
                session.add(user)
                session.commit()
                return user.id
        except Exception as e:
            print(e)
    
    @staticmethod
    def get_user(**kwargs):
        try:
            with session:
                id = kwargs['id']
                address = subqueryload(User.address)
                user = session.query(User).options(address).filter(User.id==id).scalar()
                return user
        except Exception as e:
            print(e)

    @staticmethod
    def update_user(**kwargs):
        try:
            with session:
                id = kwargs['user']['id']
                user = session.query(User).filter(User.id==id).scalar()
                columns = [c.name for c in user.__table__.columns][1:]
                for col in columns:
                    if col in kwargs['user']:
                        setattr(user, col, kwargs['user'][col])
                adress = user.address
                columns_address = [c.name for c in adress.__table__.columns][1:]
                for col in columns_address:
                    if col in kwargs['address']:
                        setattr(user, col, kwargs['address'][col])
                session.commit()
                return user.id
        except Exception as e:
            print(e)
    
    @staticmethod
    def delete_user(**kwargs):
        try:
            with session:
                id = kwargs['id']
                user = session.query(User).filter(User.id==id).scalar()
                session.delete(user)
                session.commit()
                return 'User deleted.'
        except Exception as e:
            print(e)

