
from functools import reduce

marks = [99, 56, 990,78, 26, 70]

print(sum(marks))

sum = 0
for i in marks:
    sum += i
print(sum)

print(max(marks))

large_num = 0
for i in marks:
    if large_num < i:
        large_num = i
else:
    print(f"large num is {large_num}")
    
    

largest = reduce(lambda a, b: a if a > b else b, marks)
print(largest)