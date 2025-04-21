'''
Demonstration of how the Policy management system works from taking
inputs from the policyholder, product and payment.
Created by : Michael Doba
'''
from policyholder import Policyholder
from product import Product
from payment import Payment

# Display details of the Policy Holder (ID, name , email, address, status, Enrolled Products, Payment History)
def display_policyholder_details(policyholder):
    print(f"Policyholder ID: {policyholder.policyholder_id}")
    print(f"Name: {policyholder.name}")
    print(f"Email: {policyholder.email}")
    print(f"Address: {policyholder.address}")
    print(f"Status: {policyholder.status}")
    print("Enrolled Products:")
    for product in policyholder.products:
        print(f"  ~ {product.name} (ID: {product.product_id}), Price: ${product.price}, Status: {product.status}")
    print("Payment History:")
    for payment in policyholder.payments:
        print(f"  ~ Payment ID: {payment.payment_id}, Product: {payment.product.name}, Amount: ${payment.amount}, Status: {payment.status}")
    print("\n")

# Create products
health_product = Product("Prod 1", "Health Insurance", "Comprehensive health coverage", 200.0)
car_product = Product("Prod 2", "Car Insurance", "Full coverage for vehicles", 1500.0)

# Create policyholders
policyholder1 = Policyholder("PH0000001", "Precious Chiutsi", "123 Snake Park, Harare", "pchiutsi@example@gmail.com")
policyholder2 = Policyholder("PH0000002", "Michael Doba", "5A Wanganui Avenue, Mabelreign, Harare", "mdoba112@gmail.com")

# Scenario when policyholder 1 purchases Health Insurance
policyholder1.add_product(health_product)
payment1 = Payment("Pmt 1", policyholder1, health_product, 200.0, "2025-01-01")
payment1.process_payment()
policyholder1.add_payment(payment1)

# Scenario when policyholder 2 purchases Car Insurance
policyholder2.add_product(car_product)
payment2 = Payment("Pmt 2", policyholder2, car_product, 2050.0, "2025-01-01")
payment2.process_payment()
policyholder2.add_payment(payment2)

# Demonstration of suspending a policyholder
policyholder1.suspend()

# Update product details
car_product.update_details(price=2250.0)

# Display details
print("Policyholder 1 Details:")
display_policyholder_details(policyholder1)

print("Policyholder 2 Details:")
display_policyholder_details(policyholder2)

# Demonstrate sending a reminder and applying a penalty for a late payment
late_payment = Payment("Pmt 3", policyholder2, car_product, 1900.0, "2025-15-01")
late_payment.send_reminder()
late_payment.apply_penalty(200.0)
late_payment.process_payment()
policyholder2.add_payment(late_payment)

# Reactivate policyholder1
policyholder1.reactivate()
print("\nAfter reactivation:")
display_policyholder_details(policyholder1)