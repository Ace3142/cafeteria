# Cafeteria Management System ⚡

A Python desktop application built with **Tkinter** and **MySQL** for managing cafeteria operations. This system allows users to view the menu, place orders, and track quantities, while admins can monitor all orders, update order status, and calculate total earnings.

---

## Features

### User Side:
- Browse cafeteria menu with prices.
- Select multiple items and specify quantities.
- Place orders that are automatically saved in the MySQL database.
- View a summary of the order with total cost.

### Admin Side:
- View all orders in a table format.
- Track order IDs, items, quantities, price per item, and total per order.
- Refresh the order list to see new orders.
- Calculate total earnings from all orders.

---

## Technologies Used
- **Python 3**
- **Tkinter** for GUI
- **Pillow** for image handling
- **MySQL (via PyMySQL)** for storing order data

---

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/cafeteria-management.git
   cd cafeteria-management
Install required Python package
 pip install tkinter pillow pymysql

Set up My sql database
create a database name cafe.
create a table name cafeteria:
CREATE TABLE cafeteria (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item VARCHAR(100),
    quantity INT,
    price FLOAT
);

Update database Credential
 Open the Python script and update the MySQL user, password, and host if necessary.

Run the application
python cafeteria_app.py


Author

[ACE] – Developed this Zenitsu-themed Cafeteria Management System in Python.



