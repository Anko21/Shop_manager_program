class Item:
    def __init__(self, id, item_name, price, stock_quantity, orders = None):
        self.id = id
        self.item_name = item_name
        self.price = price
        self.stock_quantity = stock_quantity
        self.orders= orders or []

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Item({self.id}, {self.item_name}, {self.price}, {self.stock_quantity}, {self.orders})"
