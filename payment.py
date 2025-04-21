'''
Policy management system class creation for the payments.
Created by : Michael Doba
'''
#payment.Py
class Payment:
    def __init__(self, payment_id, policyholder, product, amount, due_date):
        self.payment_id = payment_id
        self.policyholder = policyholder
        self.product = product
        self.amount = amount
        self.due_date = due_date
        self.status = "pending"
        self.penalty_applied = False

    def process_payment(self):
        self.status = "paid"

    # Send reminder to Policy members with outstanding Payments.
    def send_reminder(self):
        print(f"Reminder sent to {self.policyholder.name} for payment {self.payment_id} due on {self.due_date}.")

    # Apply penalty and show outstanding new amount
    def apply_penalty(self, penalty_amount):
        if self.status != "paid" and not self.penalty_applied:
            self.amount += penalty_amount
            self.penalty_applied = True
            print(f"Penalty of {penalty_amount} applied to payment {self.payment_id}. New amount: {self.amount}")