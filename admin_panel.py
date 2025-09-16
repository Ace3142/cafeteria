import tkinter as tk
from tkinter import ttk, messagebox
import pymysql

class AdminPanel:
    def __init__(self, root):
        self.root = root
        self.root.title("🔑 Admin Panel")
        self.root.geometry("700x500")
        self.root.configure(bg="#FFF9C4")

        title = tk.Label(
            root,
            text="📊 Admin Dashboard",
            font=("Poppins", 18, "bold"),
            bg="#FFF9C4"
        )
        title.pack(pady=10)

        # Treeview for orders
        columns = ("id", "item", "quantity", "price")
        self.tree = ttk.Treeview(root, columns=columns, show="headings", height=15)
        for col in columns:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=150, anchor="center")
        self.tree.pack(pady=10, fill="both", expand=True)

        # Buttons
        btn_frame = tk.Frame(root, bg="#FFF9C4")
        btn_frame.pack(pady=10)

        refresh_btn = ttk.Button(btn_frame, text="🔄 Refresh", command=self.load_orders)
        refresh_btn.grid(row=0, column=0, padx=10)

        total_btn = ttk.Button(btn_frame, text="💰 Total Earnings", command=self.show_total)
        total_btn.grid(row=0, column=1, padx=10)

        # Load orders initially
        self.load_orders()

    def load_orders(self):
        # Clear tree first
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Connect to DB and fetch orders
        con = pymysql.connect(
            host="localhost",
            user="root",
            password="database",  # your MySQL password
            database="cafe"
        )
        cur = con.cursor()
        cur.execute("SELECT id, item, quantity, price FROM cafeteria")
        rows = cur.fetchall()
        con.close()

        # Insert into treeview
        for row in rows:
            self.tree.insert("", "end", values=row)

    def show_total(self):
        con = pymysql.connect(
            host="localhost",
            user="root",
            password="database",
            database="cafe"
        )
        cur = con.cursor()
        cur.execute("SELECT SUM(price) FROM cafeteria")
        total = cur.fetchone()[0]
        con.close()
        total = total if total else 0
        messagebox.showinfo("Total Earnings", f"💰 Total Earnings so far: ₹{total}")
