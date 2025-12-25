

friends = ["Apple","banana",67.8,False,"Python"];
print(friends);
friends.append("Kiwi");
print(friends);


nums = [2,6,7,22,0,345,10];
# newNums = nums.sort();
print(nums);
# print(newNums); #returns none because sort directly changes original nums
nums.sort();
print(nums);
nums.insert(3,999);
print(nums);

nums.pop(3);
print(nums);

nums.remove(345);
print(nums);



numbers = [90,67,126,4,7,87,1];
newNumbers = sorted(numbers);
print(numbers);
# print(sorted(numbers));
print(newNumbers);





# | Method         | Changes original list | Returns value |
# | -------------- | --------------------- | ------------- |
# | `list.sort()`  | ✅ Yes                 | ❌ None        |
# | `sorted(list)` | ❌ No                  | ✅ New list    |
