from lib.item import *
from lib.item_repository import *

def test_get_all_item_records(db_connection): 
    db_connection.seed("seeds/items_orders.sql")
    repository = ItemRepository(db_connection) 
    
    items = repository.all() 
    
    assert items == [
        Item(1, 'Dog treats', 5, 50),
        Item(2, 'Dog Collars', 25, 42),
        Item(3, 'Dog beds', 75, 23),
        Item(4, 'Dog food', 70, 1),
        Item(5, 'Dog toys', 20, 32),
        Item(6, 'Dog blankets', 15, 56),
        Item(7, 'Dog shirts', 35, 65),
        Item(8, 'Paw Cleaner', 30, 48),
        Item(9, 'Dog Shampoo', 15, 96)
    ]

def test_create_item_record(db_connection):
    db_connection.seed("seeds/items_orders.sql") 
    repository = ItemRepository(db_connection) 
    
    repository.create(Item(10, 'Dog', 500, 1),)
    items = repository.all() 

    assert items == [
        Item(1, 'Dog treats', 5, 50, []),
        Item(2, 'Dog Collars', 25, 42, []),
        Item(3, 'Dog beds', 75, 23, []),
        Item(4, 'Dog food', 70, 1, []),
        Item(5, 'Dog toys', 20, 32, []),
        Item(6, 'Dog blankets', 15, 56, []),
        Item(7, 'Dog shirts', 35, 65, []),
        Item(8, 'Paw Cleaner', 30, 48, []),
        Item(9, 'Dog Shampoo', 15, 96, []),
        Item(10, 'Dog', 500, 1, [])
    ]