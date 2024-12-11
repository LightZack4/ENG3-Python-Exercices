
price = float(input("Please type in a price: "))


dinars = int(price)  # Integer part
centimes = round((price - dinars) * 100)  


print(f"Dinars: {dinars}")
print(f"Centimes: {centimes}")
