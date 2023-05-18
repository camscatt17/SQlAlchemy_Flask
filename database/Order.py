from __init__ import engine, session, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker, subqueryload
from sqlalchemy import Table, event

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