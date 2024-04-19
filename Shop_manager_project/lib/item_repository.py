from lib.item import *

class ItemRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * from items')
        items = []
        for row in rows:
            item = Item(row['id'], row["item_name"], row["price"], row["stock_quantity"])
            items.append(item)
        return items
    
    # def find(self,artist_id):
    #     rows = self.connection.execute(
    #         'SELECT * from albums WHERE artist_id = %s', [artist_id]
    #     )
    #     albums = []
    #     for row in rows:
    #         item = Album(row['id'], row["title"], row["release_year"], row["artist_id"])
    #         albums.append(item)

        # return albums
    
    def create(self, item):
        self.connection.execute(
            'INSERT INTO items (id, item_name, price, stock_quantity) VALUES(%s,%s,%s,%s)',[
                item.id, item.item_name, item.price, item.stock_quantity
            ]
        )
