# Insurance Policy Management System

A Python-based system to manage policyholders, insurance products, and payments.  
Built with object-oriented programming (OOP) principles for modularity and scalability.

---

## 📋 Table of Contents
- [Overview](#-overview)
- [Key Features](#-key-features)
- [Class Structure](#-class-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Output Explanation](#-output-explanation)
- [OOP Principles Demonstrated](#-oop-principles-demonstrated)
- [Common Errors & Solutions](#-common-errors--solutions)
- [Contribution Guidelines](#-contribution-guidelines)
---

## 🌟 Overview
This system models core insurance operations using three interconnected classes:
- *Policyholder*: Manages customer details, status, and enrolled products.
- *Product*: Represents insurance offerings (e.g., Health/Car Insurance) with dynamic pricing.
- *Payment*: Handles transactions, reminders, and penalties for overdue payments.

---

## 🔑 Key Features

### Policyholder Management
- Register, suspend, or reactivate policyholders.
- Track enrolled products and payment history.

### Product Management
- Create/update insurance products.
- Suspend or reactivate products dynamically.
### Payment Management
- Process payments with late penalties.
- Automated reminders and status tracking.

---

## 🏗 Class Structure

### Policyholder Class (policyholder.py)
| *Attribute/Method*       | *Description*                                  |
|----------------------------|--------------------------------------------------|
| policyholder_id, name  | Unique ID and name of the policyholder.          |
| status                   | active or suspended.                         |
| add_product(product)     | Enroll in a new insurance product.               |
| suspend() / reactivate()| Change policyholder status.                     |

### Product Class (product.py)
| *Attribute/Method*       | *Description*                                  |
|----------------------------|--------------------------------------------------|
| product_id, price      | Unique ID and cost of the product.               |
| update_details(...)      | Modify product name, description, or price.      |
| status                   | available or suspended.                      |

### Payment Class (payment.py)
| *Attribute/Method*       | *Description*                                  |
|----------------------------|--------------------------------------------------|
| amount, due_date       | Payment amount and deadline.                     |
| process_payment()        | Mark payment as paid.                          |
| apply_penalty(penalty)   | Add late fees to unpaid payments.                |

---

## 🛠 Installation
1. *Requirements*: Python 3.6+.
2. *Clone the repository*:
   ```bash
   git clone https://github.com/MichaelDoba/Python-and-R-by-MD-3.git
   cd insurance-policy-system

   
3. **Run the demo**:
   bash
   python demo.py
   
---

## 🚀 Usage
python
# Create a product
car_insurance = Product("Prod 2", "Car Insurance", "Accident coverage", 150.0)

# Register a policyholder
john = Policyholder("PH0000003", "John Doe", "789 Pine Rd", "john@email.com")

# Enroll in product and process payment
payment = Payment("Pmt 4", john, car_insurance, 150.0, "2025-04-21")
payment.process_payment()
john.add_payment(payment)
john.add_product(car_insurance)

## 📊 Output Explanation
Running `demo.py` will display:

Policyholder Details:
- Status: Active/Suspended
- Enrolled Products: Product name, price, and availability status.
- Payments: Amount paid, penalties (if any), and payment status.
---

## 🧠 OOP Principles Demonstrated
1. **Encapsulation**: Each class encapsulates its own data and logic.  
   Example: `Payment` handles penalties internally via `apply_penalty()`.
2. **Separation of Concerns**: Dedicated classes for policyholders, products, and payments.
3. **Reusability**: Methods like `update_details()` allow easy modifications.
---
 ## 🚨 Common Errors & Solutions
| **Error**                                  | **Solution**                                   |
|-------------------------------------------|------------------------------------------------|
| `ModuleNotFoundError`                     | Ensure filenames match imports exactly (case-sensitive!). |
| `TypeError: Product() takes no arguments` | Verify `__init__` method in `Product` class.   |
| `AttributeError`                          | Check method names/indentation in class files. |

---

## 🤝 Contribution Guidelines
1. Fork the repository.
2. Add tests for new features (e.g., `test_policyholder.py`).
3. Submit a pull request with a clear description of changes.

---
  
