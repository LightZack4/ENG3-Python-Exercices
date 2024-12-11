
total_amount = float(input("Total amount: "))
num_items = int(input("Number of items: "))
day_of_week = input("Day of the week: ").lower()


if day_of_week in ["saturday", "sunday"]:
    discount = 0.20  
else:
    discount = 0.10  

if num_items > 5:
    additional_discount = 0.05  
else:
    additional_discount = 0.00


total_discount = discount + additional_discount


discounted_price = total_amount * (1 - total_discount)


print(f"Total price after discount: {discounted_price} dinars")
