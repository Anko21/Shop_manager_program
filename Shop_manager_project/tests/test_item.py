from lib.item import *

def test_item_constructs():
    item = Item(1, 'Dog treats', 5, 50)
    assert item.id == 1
    assert item.item_name == 'Dog treats'
    assert item.price == 5
    assert item.stock_quantity == 50

def test_item_format_nicely():
    item = Item(1, 'Dog treats', 5, 50)
    assert str(item) == 'Item(1, Dog treats, 5, 50, [])'


def test_item_are_equal():
    item_1 = Item(1, 'Dog treats', 5, 50)
    item_2 = Item(1, 'Dog treats', 5, 50)
    assert item_1 == item_2