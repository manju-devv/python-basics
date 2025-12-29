my_set = {1,4,2,9};
print(my_set);

my_set.add("manju");
print(my_set);

my_set.add(10);
print(my_set);

my_set.add(True);  #it wont add true because py treats True == 1 and false == 0 and 1 is already present and py wont allow duplicates
print(my_set);

my_set.add(False);  #it ll add False 
print(my_set);



my_set.update([11,12,13,"pythonn"]);    #to add multiple items in set 
print(my_set);


# remove()
# Removes element (error if not found)

my_set.remove(2);
print(my_set);



# discard()
# Removes element (no error)

my_set.discard(2);
print(my_set);



# pop()
# Removes and returns a random element

my_set.pop();     #its removing 1st element
print(my_set);


# my_set.clear();      #clears entire set
# print(my_set);