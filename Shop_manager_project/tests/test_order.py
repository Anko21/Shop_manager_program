from lib.order import *

def test_order_constructs():
    order = Order(1, 'Anna' , '2024-05-19')
    assert order.id == 1
    assert order.customer_name == 'Anna'
    assert order.order_date == '2024-05-19'

def test_order_format_nicely():
    order = Order(1, 'Anna' , '2024-05-19')
    assert str(order) == 'Order(1, Anna, 2024-05-19, [])'


def test_item_are_equal():
    order_1 = Order(1, 'Anna' , '2024-05-19')
    order_2 = Order(1, 'Anna' , '2024-05-19')
    assert order_1 == order_2