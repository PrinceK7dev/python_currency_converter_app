import tkinter as tk
from tkinter import ttk, messagebox
import requests

def get_rates():
    """Fetch live exchange rates"""
    try:
        response = requests.get("https://api.frankfurter.app/latest")
        data = response.json()
        rates = data['rates']
        rates['EUR'] = 1.0  # Base is EUR
        return rates
    except:
        messagebox.showerror("Error", "Failed to fetch exchange rates!")
        return None

def convert_currency():
    """Convert currency based on user selection"""
    rates = get_rates()
    if rates is None:
        return
    
    from_curr = from_currency.get()
    to_curr = to_currency.get()
    try:
        amount_val = float(amount_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")
        return

    if from_curr not in rates or to_curr not in rates:
        messagebox.showerror("Error", "Currency not supported!")
        return

    eur_amount = amount_val / rates[from_curr]
    result = eur_amount * rates[to_curr]
    result_label.config(text=f"{amount_val:.2f} {from_curr} = {result:.2f} {to_curr}")

# Create main window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")
root.resizable(False, False)

# Title label
title_label = tk.Label(root, text="Currency Converter", font=("Helvetica", 16))
title_label.pack(pady=10)

# Frame for inputs
frame = tk.Frame(root)
frame.pack(pady=10)

# Amount
amount_label = tk.Label(frame, text="Amount:")
amount_label.grid(row=0, column=0, padx=5, pady=5)
amount_entry = tk.Entry(frame)
amount_entry.grid(row=0, column=1, padx=5, pady=5)

# From Currency
from_label = tk.Label(frame, text="From:")
from_label.grid(row=1, column=0, padx=5, pady=5)
from_currency = ttk.Combobox(frame, values=["USD", "EUR", "INR", "JPY", "GBP"])
from_currency.grid(row=1, column=1, padx=5, pady=5)
from_currency.current(0)

# To Currency
to_label = tk.Label(frame, text="To:")
to_label.grid(row=2, column=0, padx=5, pady=5)
to_currency = ttk.Combobox(frame, values=["USD", "EUR", "INR", "JPY", "GBP"])
to_currency.grid(row=2, column=1, padx=5, pady=5)
to_currency.current(1)

# Convert Button
convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.pack(pady=20)

# Result Label
result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

root.mainloop()
