a = int(input("enter 1st num: "));
b = int(input("enter 2nd num: "));
c = a + b;
print(f'sum of two num is: {c}')


a = 27;
b = 4;
c = a % b;
print(f"the remainder of {a} & {b} is {c}");


a = int(input("enter a num: "));
b = int(input("enter b num: "));
if(a > b):
    print(f"{a} is greater than {b}");
else:
    print(f"{b} is greater than {a}");



a = int(input("enter num1: "));
b = int(input("enter num2: "));
c = (a + b)/2
print(f"Average : {c}");


n = int(input("enter how many numbers: "));
numbers = [];
for i in range(n):
    num = int(input(f"enter num {i+1}: "));
    numbers.append(num);

average = sum(numbers)/len(numbers);     # average = sum(numbers)/n; 
print(f"average of {numbers} is : {average}");


a = int(input("enter a num: "));
print (f"square of {a} is {a ** 2}")