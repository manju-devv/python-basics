# multiplication using for loop


for i in range(11):
    if i == 0:
        continue
    print(f"{5} * {i} = {5*i}")


print("========>")

num = int(input("enter number: "))
for i in range(1, 11):
    print(f"{num} X {i} = {num * i}")


l = ["sonam", "Harry", "somu", "Bablu"]
for name in l:
    if name.startswith("s"):
        print(f"Hello {name}")


# check prime or not

num = int(input("enter a num: "))
for i in range(2, num):
    if num % i == 0:
        print(f"yout number {num} is not prime")
        break
else:
    print(f"your number {num} is a prime")


print("<========>")

sum_num = int(input("enter number: "))
i = 0
sum = 0

while i <= sum_num:
    sum += i
    i += 1

print(f"sum of numbers upto {sum_num} : {sum}")
print(f"sum = {(sum_num*(sum_num + 1)/2)}")


print("<========>")

fact = int(input("enter number: "))
prod = 1;
for i in range(1, fact+1):
    prod = prod * i;
else:
    print(f"factorial of {fact} is {prod}")
