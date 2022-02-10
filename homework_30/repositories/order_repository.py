from .base_repository import BaseRepository
from ..models import Order
from typing import List


class OrderRepository(BaseRepository):
    def get_all_order(self) -> List[Order]:
        return self._session.query(Order).all()

    def get_order_by_id(self, id: str) -> Order:
        return self._session.query(Order).filter(Order.id == id).first()

    def add_order(self, data: dict) -> None:
        self._session.add(Order(**data))

    def change_quantity_by_id(self, id: str, quantity: int) -> None:
        self._session.query(Order).filter(Order.id == id).update({"quantity": quantity})

    def change_product_by_id(self, id: str, products_id: str) -> None:
        self._session.query(Order).filter(Order.id == id).update({"products_id": products_id})

    def change_delivery_order_by_id(self, id: str, delivery_order: str) -> None:
        self._session.query(Order).filter(Order.id == id).update({"delivery_order": delivery_order})

    def change_status_order_by_id(self, id: str, status_order: str) -> None:
        self._session.query(Order).filter(Order.id == id).update({"status_order": status_order})

    def change_payment_order_by_id(self, id: str, payment_status: str) -> None:
        self._session.query(Order).filter(Order.id == id).update({"payment_status": payment_status})

    def change_parameters_by_id(self, id: str, update_data: dict) -> None:
        self._session.query(Order).filter(Order.id == id).update(update_data)

    def delete_order_by_id(self, id: str) -> None:
        self._session.query(Order).filter(Order.id == id).delete()
