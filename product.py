'''
Policy management system class creation for the products.
Created by : Michael Doba
'''
#product.py
class Product:
    def __init__(self, product_id, name, description, price):  # Parameters added
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.status = "available"  # Status initialized

    def update_details(self, name=None, description=None, price=None):
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if price is not None:
            self.price = price

    def suspend(self):
        self.status = "suspended"

    def activate(self):
        self.status="available"