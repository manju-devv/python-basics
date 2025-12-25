try:
    no_of_fruits = int(input("Enter num of Fruits: "))
except ValueError:
    print("please enter a number")
    exit()

fruits = []

for i in range(no_of_fruits):
    fruit = input("Enter fruit: ")
    fruits.append(fruit)
print(f"fruits are: {fruits}")


# Python doesn’t check types after conversion like JS — it fails during conversion.
# So:
# JS → check type after input
# Python → handle the error during conversion


nums = [1, 2, 3, 4, 5]
print(sum(nums))

total = 0
for i in nums:
    total += i
print(total)


nums = [1, 2, 3, 4, 5]
total = 0
i = 0

while i < len(nums):
    total += nums[i]
    i += 1
print(total)
