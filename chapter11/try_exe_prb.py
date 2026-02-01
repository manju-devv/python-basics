try:
    with open("1.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)


try:
    with open("2.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

print("Thank you!!")


num_list = [1, 3, 5, 7, 9, 11, 13, 17]

for i, item in enumerate(num_list):
    if i == 2 or i == 4 or i == 6:
        print(item)
