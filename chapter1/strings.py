# strings are immutable

name = "manju";

print(len(name));
print(name[0:3]);

# negative slicing

name = "America";
print(name[-5: -1]);
print(name[2:6]);

# skip
numbers = "123456789";
print(numbers[1:8]);
# print(numbers[1:8:2]);  skips 2 characters starting with 1st one [or just remove 2-1=1 skip 1 character each]
