a = int(input("enter a number: "))

table = [a * i for i in range(1, 11)]
with open("table.txt", "a") as f:
    f.write(f"table of {a} - {str(table)} \n")
