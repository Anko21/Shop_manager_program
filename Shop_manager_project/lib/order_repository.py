from lib.order import *

class OrderRepository:
    def __init__(self, connection):
        self.connection = connection
    
    def all(self):
        rows = self.connection.execute('SELECT * from orders')

        orders = []
        for row in rows:
            item = Order(row['id'], row["customer_name"], row['order_date'])
            orders.append(item)
        
        return orders
    
    def create(self, order):
        self.connection.execute(
            'INSERT INTO orders (id, customer_name, order_date) VALUES(%s,%s,%s)',
            [order.id, order.customer_name, order.order_date])
