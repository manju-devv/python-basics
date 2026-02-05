from functools import reduce

l = [1, 2, 3, 4, 5, 6]

sq = lambda x: x * 2

sqList = map(sq, l)
print(list(sqList))


evenNums = list(filter(lambda x: x % 2 == 0, l))
print(evenNums)


def sumNums(a, b):
    return a + b


reduceNums = reduce(sumNums, l)
print(reduceNums)


newNums = reduce(lambda a, b: a + b, l)
print(newNums)
