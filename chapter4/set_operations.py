# Sets are unordered
# No duplicates
# Mutable (but elements must be immutable)
# No indexing: s[0] err



set1 = {"adam","bob","catherin"};
set2 = {"bob","david"};


# union() operator or | . gives all users
print(set1 | set2);
print(set1.union(set2));
# print(set1 | set1);

# intersection() or &.    gives common users [present in both]
print(set1 & set2);
print(set1.intersection(set2));
# print(set1 & set1);


# difference() or -    removes common elements gives users only in first set or second set based on usage

print(set1 - set2);
print(set2.difference(set1));

print(set1-set1);    #removes all elements and gives empty set


# symmetric_difference() or ^ ----> “Unique elements from both sets”

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.symmetric_difference(B))
print(A ^ B)


print(len(set1));




# issubset() -----> All elements of A are inside B

A = {1,2};
B = {4,3,2,1}

print(A.issubset(B));  #true since all elements of a are in b
print(B.issubset(A));  #false since all elements of b are not  in a



# issuperset()  ----->  C contains all elements of D

C = {1,2};
D = {1,2,3,4};

print(C.issuperset(D));
print(D.issuperset(C));


# isdisjoint() -------> No common elements at all

E = {1,2,3};
F = {4,5,6};
print(E.isdisjoint(F));
print(F.isdisjoint(F));        #------> returns false since it compares same set and ele are same 
print(F.isdisjoint(E));

