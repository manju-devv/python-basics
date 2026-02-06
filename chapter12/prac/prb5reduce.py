from functools import reduce

nums = [1, 2, 3, 4, 5]

sumOfNums = reduce(lambda x, y: x + y, nums)

print(sumOfNums)


def findMax(x, y):
    return x if x > y else y

funcNums = reduce(findMax, nums)
print(funcNums)


numsss = [3, 7, 2, 9, 5]

max_num = reduce(lambda x, y: x if x > y else y, numsss)
print(max_num)
print(max(numsss))