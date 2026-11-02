
# Reflection 1:
# The most surprising thing about Python lists is that they can be changed after
# they are created. You can add, remove, and rearrange items whenever you need to.

# Reflection 2:
# At Yogurtology, a Python list could help keep track of supplies like cups,
# spoons, and toppings. It could make counting items and checking supplies
# easier than doing everything manually in Excel.

# EXERCISE 1
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# EXERCISE 2
print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])

# EXERCISE 3
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# EXERCISE 4
inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

# EXERCISE 5
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("Tuples are useful for coordinates because their values cannot be changed.")

print(coords)

# EXERCISE 6
sales = [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
average = total / count

print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", max(sales))
print("Worst:", min(sales))

# EXERCISE 7
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    discounted.append(round(price * 0.90, 2))

print(prices)
print(discounted)

# EXERCISE 8
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print(high_sales)
print("Count:", len(high_sales))
print("Avg:", sum(high_sales) / len(high_sales))
