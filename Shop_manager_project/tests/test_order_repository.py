from lib.order import *
from lib.order_repository import *
import datetime
def test_get_all_order_records(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    repository = OrderRepository(db_connection)

    orders = repository.all()
    assert orders == [
        Order(1, 'Anna' , datetime.date(2024, 5, 19)),
        Order(2, 'Rachel', datetime.date(2024, 5, 19)),
        Order(3, 'Tom', datetime.date(2024, 8, 23)),
        Order(4, 'John', datetime.date(2024, 2, 14)),
        Order(5, 'Thomas', datetime.date(2024, 6, 18)),
        Order(6, 'Paul', datetime.date(2024, 1, 19)),
        Order(7, 'Steve', datetime.date(2024, 7, 12)),
        Order(8, 'Hunor', datetime.date(2024, 6, 11)),
        Order(9, 'Eoin', datetime.date(2024, 8, 26)),
        Order(10, 'Jen', datetime.date(2024, 3, 29)),
        Order(11, 'Selva', datetime.date(2024, 2, 15)),
    ]

def test_create_new_order(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    repository = OrderRepository(db_connection)
    repository.create(Order(12, 'Greg' , datetime.date(2024, 3, 25)))
    
    orders = repository.all()
    assert orders == [
        Order(1, 'Anna' , datetime.date(2024, 5, 19)),
        Order(2, 'Rachel', datetime.date(2024, 5, 19)),
        Order(3, 'Tom', datetime.date(2024, 8, 23)),
        Order(4, 'John', datetime.date(2024, 2, 14)),
        Order(5, 'Thomas', datetime.date(2024, 6, 18)),
        Order(6, 'Paul', datetime.date(2024, 1, 19)),
        Order(7, 'Steve', datetime.date(2024, 7, 12)),
        Order(8, 'Hunor', datetime.date(2024, 6, 11)),
        Order(9, 'Eoin', datetime.date(2024, 8, 26)),
        Order(10, 'Jen', datetime.date(2024, 3, 29)),
        Order(11, 'Selva', datetime.date(2024, 2, 15)),
        Order(12, 'Greg' , datetime.date(2024, 3, 25))
    ]