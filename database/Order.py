import datetime
from __init__ import session, Base
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Table, event
from sqlalchemy.orm import  relationship, subqueryload
from User import User
from Product import Product

order_product = Table('order_product', Base.metadata,
                      Column('order_id', Integer, ForeignKey('order.id')),
                      Column('product_id', Integer, ForeignKey('product.id'))
                    )

class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', backref='order_user', cascade='all, delete')
    product = relationship('Product', secondary=order_product, backref='order_product')

    def __repr__(self):
        return f'<Order(id={self.id}, date={self.date}, uder={self.uder}, product={self.product})'
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
## Delete many-to-many
@event.listens_for(Order, 'after_delete')
def delete_order_product(mapper, connection, target):
    connection.execute(order_product.delete().where(order_product.c.oder_id == target.id))


class Queries():
    @staticmethod
    def add_order(**kwargs):
        try:
            with session:
                order = Order()
                columns = [c.name for c in order.__table__.columns][1:]
                for col in columns:
                    if col in kwargs:
                        setattr(order, col, kwargs[col])
                user_id = kwargs['user'][id]
                user = session.query(User).filter(User.id==user_id).scalar()
                order.date = datetime.now()
                order.user = user
                for id in kwargs['product_ids']:
                    product = session.query(Product).filter(Product.id==id).scalar()
                    order.product.append(product)
                session.add(order)
                session.commit()
                return order.id
        except Exception as e:
            print(e)
    
    @staticmethod
    def get_order_by_user(**kwargs):
        try:
            with session:
                user_id = kwargs['user']['id']
                product = subqueryload(Order.product)
                user = subqueryload(Order.user).subqueryload(User.address)
                order = session.query(Order).filter(Order.user_id==user_id).all()
                user = session.query(Order).options(product, user).filter(User.id==id).scalar()
                return order
        except Exception as e:
            print(e)

    @staticmethod
    def get_order(**kwargs):
        try:
            with session:
                id = kwargs['id']
                product = subqueryload(Order.product)
                user = subqueryload(Order.user).subqueryload(User.address)
                order = session.query(Order).filter(Order.user_id==user_id).all()
                user = session.query(Order).options(product, user).filter(User.id==id).scalar()
                return order
        except Exception as e:
            print(e)
    
    @staticmethod
    def delete_order(**kwargs):
        try:
            with session:
                id = kwargs['id']
                order = session.query(Order).filter(Order.id==id).scalar()
                session.delete(order)
                session.commit()
                return 'Order deleted.'
        except Exception as e:
            print(e)

## Order
## Add order
# data = {
#    'user':{'id':1},
#    'product_ids': [1, 3, 5]
# }
# add = Queries.add_order(**data)
# print(add)

## Get order by user
# data = {'user': {'id': 1}} 
# get = Queries.get_order_by_user(**data)
# print(get)

## Delete user
# data = {'id':1}
# delete = Queries.delete_order(**data)
#print(delete)
   