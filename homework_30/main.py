from homework_30.repositories import OrderRepository

# e.g. CRUD operations
repository = OrderRepository()

# get all orders (Read operation)
orders = repository.get_all_order()
for order in orders:
    print(order)
print('*' * 100)

# add new order to DB (Create operation)
repository.add_order(
    {
        "id": "A9119",
        "products_id": "P2000",
        "quantity": 77,
        "delivery_order": "arrived",
        "status_order": "open",
        "payment_status": "paid"
    }
)
orders = repository.get_all_order()
for order in orders:
    print(order)
print('*' * 100)

# get order by id (Read operation)
order = repository.get_order_by_id('A9119')
print(order)
print('*' * 100)

# change order parameters by id (Update operation)
repository.change_product_by_id('A1000', 'P1111')
repository.change_quantity_by_id('A1000', 11)
repository.change_delivery_order_by_id('A1000', 'shipped')
repository.change_status_order_by_id('A1000', 'canceled')
repository.change_payment_order_by_id('A1000', 'failed')
print(repository.get_order_by_id('A1000'))
print('*' * 100)

# change some parameters by id (Update operation)
repository.change_parameters_by_id('A1000',
                                   {
                                       "products_id": "P4444",
                                       "quantity": 44,
                                       "delivery_order": "returned",
                                       "status_order": "completed",
                                       "payment_status": "unpaid"
                                   }
                                   )
print(repository.get_order_by_id('A1000'))
print('*' * 100)

# delete created order by id (Delete operation)
repository.delete_order_by_id('A9119')
orders = repository.get_all_order()
for order in orders:
    print(order)
