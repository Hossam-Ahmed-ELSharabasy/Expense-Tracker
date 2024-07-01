import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import requests

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        # Labels and Entries
        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_label.grid(row=0, column=0)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=0, column=1)

        self.currency_label = tk.Label(root, text="Currency:")
        self.currency_label.grid(row=1, column=0)
        self.currency_combobox = ttk.Combobox(root, values=["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD"])
        self.currency_combobox.grid(row=1, column=1)

        self.category_label = tk.Label(root, text="Category:")
        self.category_label.grid(row=2, column=0)
        self.category_combobox = ttk.Combobox(root, values=["Life expenses", "Electricity", "Gas", "Rental", "Grocery", "Savings", "Education", "Charity"])
        self.category_combobox.grid(row=2, column=1)

        self.date_label = tk.Label(root, text="Date:")
        self.date_label.grid(row=3, column=0)
        self.date_entry = tk.Entry(root)
        self.date_entry.grid(row=3, column=1)

        self.payment_label = tk.Label(root, text="Payment Method:")
        self.payment_label.grid(row=4, column=0)
        self.payment_combobox = ttk.Combobox(root, values=["Cash", "Credit Card", "Paypal"])
        self.payment_combobox.grid(row=4, column=1)

        # Add Expense Button
        self.add_button = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_button.grid(row=5, column=0, columnspan=2)

        # Expense Table
        self.tree = ttk.Treeview(root, columns=("Amount", "Currency", "Category", "Date", "Payment Method"), show="headings")
        self.tree.heading("Amount", text="Amount")
        self.tree.heading("Currency", text="Currency")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Payment Method", text="Payment Method")
        self.tree.grid(row=6, column=0, columnspan=2)

        # Total Expense Label
        self.total_label = tk.Label(root, text="Total: $0.00")
        self.total_label.grid(row=7, column=0, columnspan=2)

    def add_expense(self):
        amount = self.amount_entry.get()
        currency = self.currency_combobox.get()
        category = self.category_combobox.get()
        date = self.date_entry.get()
        payment_method = self.payment_combobox.get()

        # Validate inputs
        if not amount or not currency or not category or not date or not payment_method:
            messagebox.showerror("Input Error", "All fields are required")
            return
        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Input Error", "Amount must be a number")
            return

        # Add expense to the table
        self.tree.insert("", tk.END, values=(amount, currency, category, date, payment_method))

        # Convert currency to USD and update total
        total = self.convert_to_usd(amount, currency)
        current_total = float(self.total_label.cget("text").split("$")[1])
        new_total = current_total + total
        self.total_label.config(text=f"Total: ${new_total:.2f}")

    def convert_to_usd(self, amount, currency):
        # Here you would use the requests library to get the current exchange rate
        # For simplicity, we'll assume a mock conversion rate
        conversion_rates = {
            "USD": 1.0,
            "EUR": 1.1,  # Mock rate: 1 EUR = 1.1 USD
            "GBP": 1.3,  # Mock rate: 1 GBP = 1.3 USD
            "JPY": 0.009,  # Mock rate: 1 JPY = 0.009 USD
            "AUD": 0.75,  # Mock rate: 1 AUD = 0.75 USD
            "CAD": 0.8,   # Mock rate: 1 CAD = 0.8 USD
            "CHF": 1.05,  # Mock rate: 1 CHF = 1.05 USD
            "CNY": 0.15,  # Mock rate: 1 CNY = 0.15 USD
            "SEK": 0.1,   # Mock rate: 1 SEK = 0.1 USD
            "NZD": 0.7    # Mock rate: 1 NZD = 0.7 USD
        }
        return amount * conversion_rates.get(currency.upper(), 1.0)

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()

