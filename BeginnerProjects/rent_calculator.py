rent = int(input("Enter amount for flat/hostel: "))
food_expenses = int(input("Enter amount spent on food: "))
electricty = int(input("Enter total electricty units spent: "))
unit_charge = int(input("Enter charge per unit on electricty: "))
persons = int(input("Enter total persons in flat/hostel: "))


electricty_amount = electricty * unit_charge
pay_per_person = (rent + food_expenses + electricty_amount) // persons

print(f"total amount each person to pay: {pay_per_person}")
