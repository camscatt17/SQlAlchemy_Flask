from sqlalchemy import text, and_
from __init__ import session, Base
from database import Product

## Retorno de todos os produtos
# Primeira forma
product = session.query(Product).from_statement(text("SELECT * FROM product")).all()
print(product)

# Segunda forma
product = session.query(Product).all()
print(product)

product = session.query(Product).filter(and_(Product.price > 50, Product.price < 1000)).all()
print(product)
