# flatten list
nestedList = [1, [2, 3], 4, [5, 6]]
flattenList = []

for i in range(len(nestedList)):
    if type(nestedList[i]) == list:
        temp = nestedList[i]
        for j in range(len(temp)):
            flattenList.append(temp[j])
    else:
        flattenList.append(nestedList[i])


print(flattenList)


result = 0
for i in range(5):
    result += i
    i += 5  # internally changes the i value but does not affect the range 0,1,2,3,4
print(result)


a = "3"
a *= 2
print(int(a) + 5)

names = ["Nithish", "Ravi", "Aman"]
for n in names:
    print(n[0])
    
animal = names.reverse()
print(animal); #none


x,y = y,x = 1,2
print(x,y)



