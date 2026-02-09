import random

fruits = ["apple", "banana"]

fruits.append("kiwi")

print(fruits)

fruits.extend(["jack fruit", "pomegranate", "avcado"])
print(fruits)


names = ["angela", "bob", "john", "patrick"]

print(len(names))

bill_payer = random.randint(0, len(names) - 1)
print(f"bill paid by: {names[bill_payer]}")


fruits = [
    "Strawberries",
    "Nectarines",
    "Apples",
    "Grapes",
    "Peaches",
    "Cherries",
    "Pears",
]
fruits[-1] = "Melons"
print(fruits)
fruits.append("Lemons")
print(fruits)



fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 

dirty_dozen = [fruits, vegetables]
print(dirty_dozen[1][1])