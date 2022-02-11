from sqlalchemy import Column, VARCHAR, Integer
from ..core import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(VARCHAR(8), primary_key=True)
    products_id = Column(VARCHAR(8))
    quantity = Column(Integer)
    delivery_order = Column(VARCHAR(16))
    status_order = Column(VARCHAR(16))
    payment_status = Column(VARCHAR(16))

    def __str__(self) -> str:
        return f"{self.id} | {self.products_id} | {self.quantity} | {self.delivery_order} | {self.status_order} | " \
               f"{self.payment_status}"
