'''
Policy management system class creation for the policyholder.
Created by : Michael Doba
'''
#policyholder.py
class Policyholder:
    def __init__(self, policyholder_id, name, address, email):
        self.policyholder_id = policyholder_id
        self.name = name
        self.address = address
        self.email = email
        self.status = "active"
        self.products = []
        self.payments = []

    def suspend(self):
        self.status = "suspended"

    def reactivate(self):
        self.status = "active"

    def add_product(self, product):
        self.products.append(product)

    def add_payment(self, payment):
        self.payments.append(payment)