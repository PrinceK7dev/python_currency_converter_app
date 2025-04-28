def currency_converter():
    # Example exchange rates (as of today, these will not update automatically)
    rates = {
        "USD": 1.0,       # US Dollar
        "EUR": 0.94,      # Euro
        "INR": 83.2,      # Indian Rupee
        "JPY": 154.6,     # Japanese Yen
        "GBP": 0.81       # British Pound
    }

    print("Available currencies:", ', '.join(rates.keys()))
    
    from_currency = input("Enter the currency you have (e.g., USD): ").upper()
    to_currency = input("Enter the currency you want (e.g., INR): ").upper()
    amount = float(input("Enter the amount: "))

    if from_currency not in rates or to_currency not in rates:
        print("Invalid currency entered.")
        return

    # Convert to USD first, then to target currency
    usd_amount = amount / rates[from_currency]
    converted_amount = usd_amount * rates[to_currency]

    print(f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")

currency_converter()
