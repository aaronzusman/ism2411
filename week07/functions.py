#self assessment
#1. the first bug i saw was the total=sale replaced the ttoal instead of just adding to each sale. the ther bugs were found by reading the code and checking the errors
#2. apply_discount takes a price and the tier. it returns price after adding the discount for gold, silver, bronze. a friend could use it giving it price and tier
#3. AI disclosure: I used AI because I was stuck on a few parts of the assignment and needed help understanding the errors.

# --- Exercise 1 ---
def calculate_tax(price, rate):
    return price * rate


print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")


# --- Exercise 2 ---
def apply_discount(price, tier):
    if tier == "gold":
        discount = 0.15
    elif tier == "silver":
        discount = 0.10
    elif tier == "bronze":
        discount = 0.05
    else:
        discount = 0

    return price * (1 - discount)


for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(200, tier):.2f}")


# --- Exercise 3 ---
def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

discounted = apply_discount(200, "gold")
print(f"After gold discount: ${discounted:.2f}")

after_tax = discounted + calculate_tax(discounted, 0.07)
print(f"After tax: ${after_tax:.2f}")

print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')


# --- Exercise 4 ---
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# --- Exercise 5 ---

sales = [120, 80, 250, 175, 90]

# bug 1: total = sale replaced the total each time instead of adding
# Fix: use += to add each sale to the total
total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

# bug 2: The for loop was missing a colon
# Fix: add a colon after sales
count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

# Bug 3: The while loop went one position past the end of the list
# Fix: use < instead of <=
i = 0
while i < len(sales):
    print(sales[i])
    i += 1


# --- Exercise 6 ---
x = 100  # Global variable


def double_it():
    x = 999  # Local variable
    return x * 2


print(x)
print(double_it())
print(x)
# the x inside the function is local so needs no change. the global x outside the function