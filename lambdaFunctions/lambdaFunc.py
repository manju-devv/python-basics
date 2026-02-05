# function created using a expression using 'lambda' keyword

# lambda arguments : expression
square = lambda x: x * x

print(square(3))


sum = lambda a, b, c: a + b + c
print(sum(4, 5, 6))


nums = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, nums))
print(result)


# this above code same as below
# def double(x):
#     return x * 2

# result = list(map(double, nums))


nums = [1, 2, 3, 4, 5] 
evens = list(filter(lambda x: x % 2 == 0, nums)) 
print(evens)


