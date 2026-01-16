# Loops are used to execute a program a certain number of times.

for i in range(1, 11):
    print(i)


print("------------->")
# while loop
# only executes if condition is true until condition becomes false

i = 1
while i < 6:
    print(i)
    i += 1

print("------------->")

dup_list = [1, "manju", True, 0.5, {"a": "bottle"}, ["apple", "banana", "kiwi"]]

k = 0
while k < len(dup_list):
    print(dup_list[k])
    k += 1


print("------------->")

# for loop
# its used to iterate through a sequence like tuple,list etc


name = "Manju"
tup = (1, 2, 3, 4, "5")
for i in name:
    print(i)
print("------------->")
for z in tup:
    print(z)


# else could be used with for loop when loop is completed

z = ["a","b","c","d","e"]
for i in z:
    print(i);
else:
    print("execution completed");
