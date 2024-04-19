from lib.database_connection import DatabaseConnection
from lib.item_repository import *
from lib.order_repository import *
from lib.order import *
from lib.item import *
import datetime

class Application():
    # Connect to the database
    def __init__(self):
        self.connection = DatabaseConnection()
        self.connection.connect()
        self.connection.seed("seeds/items_orders.sql")

    def run(self):
        print('Welcome to the shop management program!')
        print(
            '''
                What would you like to do? 
                1 - List all shops items
                2 - Create a new item
                3 - List all orders
                4 - Create a new order
            '''
        )
        user_selection = int(input("Enter your choice:"))
        print(f'You selected {user_selection}')

        if user_selection == 1:
            print("Here is a list of all shop items")

            item_repository = ItemRepository(self.connection)
            items = item_repository.all()   
            for i in range(len(items)):
                print(f'{i+1}. {items[i]}')

        elif user_selection == 2:
            print("Create a new item:")
            item_id = int(input("Add id:\n"))
            item_name = input("Add items' name:\n")
            price = int(input("Add price:\n"))
            stock_quantity = int(input("Add stock_quantity:\n"))
       
            item_repository = ItemRepository(self.connection)
            items = item_repository.create(Item(item_id, item_name, price, stock_quantity))   

        elif user_selection == 3:
            print("Here is a list of all of the orders")

            order_repository = OrderRepository(self.connection)
            orders = order_repository.all()   
            for i in range(len(orders)):
                print(f'{i+1}. {orders[i]}')

        elif user_selection == 4:
            print("Create a new order:")
            order_id = int(input("Add id:\n"))
            customer_name = input("Add customer's name:\n")
            date_input = input("Add the orders date in the format YYYY-mm-dd:\n")
            order_date = datetime.datetime.strptime(date_input, '%Y-%m-%d').date()

            order_repository = OrderRepository(self.connection)
            orders = order_repository.create(Order(order_id, customer_name, order_date))   

if __name__ == '__main__':
    app = Application()
    app.run()