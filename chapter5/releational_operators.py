# relational operators [conditional operators] are used to evaluate
# condition inside if statements

# ==
# >=
# <=


# Logical operators

# and - & 
# or - |
# not 


# a = int(input("Enter how many numbers: "));
# nums = [];
# for i in range(a):
#     b = int(input("enter num:"));
#     nums.append(b);

# greatest = nums[0];
# for i in range(1,len(nums)):
#     if nums[i] > greatest:
#         greatest = nums[i]

# print(f"greatest num in {nums} is: {greatest}")


a1 = int(input("enter num1: "));
a2 = int(input("enter num2: "));
a3 = int(input("enter num3: "));

if(a1 > a2 and a1 > a3):
    print(f"great is {a1}")
elif(a2 > a1 and a2 > a3):
    print(f"great is {a2}")
else: 
    print(f"great is {a3}")