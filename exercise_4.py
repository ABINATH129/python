foods = []
prices = []
total = 0

while True:
    food = input("enter your food to buy (q to quit): ")
    if food.lower()=="q":
        break
    else:
        price = float(input("enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)
print("-----YOUR CART-----")

for food in foods:
    print(food, end=" ")
for price in prices:
    total += price
print()
print(f"your total is : ${total}")
