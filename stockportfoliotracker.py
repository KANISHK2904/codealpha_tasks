# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 300
}

total = 0

n = int(input("How many stocks do you want to enter? "))

for i in range(n):
    name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))
    
    if name in stock_prices:
        value = stock_prices[name] * quantity
        total += value
    else:
        print("Stock not found!")

print("Total Investment Value:", total)
