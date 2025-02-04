from sqlalchemy.orm import Session
from .models import Product

def delete_product(db: Session, product_id: int):
    product = db.query(Product).filter(Product.id_producto == product_id).first()
    if product:
        db.delete(product)
        db.commit()
        return True
    return False
