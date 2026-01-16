# break,continue,pass

for i in range(1, 11):
    if i == 6:
        break  # used to exit loop if condition is met
    print(i)

print("<=========>")

for j in range(1, 11):
    if j == 5:
        continue  # skip the specific itetation
    print(j)


# pass is a null statement and it tells to do nothing

l = ["apple", "banana", "jack fruit"]
for i in l:
    pass
