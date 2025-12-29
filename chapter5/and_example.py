marks1 = int(input("enter marks1: "))
marks2 = int(input("enter marks2: "))
marks3 = int(input("enter marks3: "))

total_percentage = (100 * (marks1 + marks2 + marks3)) / 300

if total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33:
    print(f"you got {total_percentage}% you are passed")
else:
    print(f"you got {total_percentage}% you are failed try next year!")


# listtt = [1,2,3,4,4]
# # print(dict.fromkeys(listtt));
# # print(type(listtt));

# print(type(listtt));
# a = list(dict.fromkeys(listtt));
# print(a);
# print(type(a));
