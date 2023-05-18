from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker, subqueryload
from sqlalchemy import Table, event
from __init__ import engine, session, Base

class Product(Base): #Criando uma tabela para o produto
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    price = Column(Float)

    def __repr__(self):
        return f'<Product(id={self.id}, name={self.name}, price={self.price}>'

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Queries():
    @staticmethod
    def add_product(**kwargs):
        try:
            with session:
                product = Product()
                columns = [c.name for c in product.__table__.columns][1:]
                for col in columns:
                    if col in kwargs:
                        setattr(product, col, kwargs[col])
            session.add(product)
            session.commit()
            return product.id
        except Exception as e:
            print(e)

    @staticmethod
    def get_product(**kwargs):
        try:
            with session:
                id = kwargs['id']
                product = session.query(Product).filter(Product.id==id).scalar()
                return product
        except Exception as e:
            print(e)

    @staticmethod
    def update_product(**kwargs):
        try:
            with session:
                id = kwargs['id']
                product = session.query(Product).filter(Product.id==id).scalar()
                columns = [c.name for c in product.__table__.columns][1:]
                for col in columns:
                    if col in kwargs:
                        setattr(product, col, kwargs[col])
                session.commit()
                return product.id
        except Exception as e:
            print(e)

    @staticmethod

    def delete_product(**kwargs):
        try:
            with session:
                id = kwargs['id']
                product = session.query(Product).filter(Product.id==id).scalar()
                session.delete(product)
                session.commit()
                return 'Product deleted.'
        except Exception as e:
            print(e)


## Products
## Add product
# data = {
#     'name':'Livro',
#     'price': 10.97
# }

# add = Queries.add_product(**data)
# print (add)


## Get product
# data = {'id': 1} 
# get = Queries.get_product(**data)
# print(get)

## Update product
# data = {
#      'id': 1,
#      'name':'Bicicleta',
#      'price': 1110.97
#  }

# upt = Queries.update_product(**data)
# print(upt)

## Delete product
# data = {'id':1}
# delete = Queries.delete_product(**data)
#print(delete)