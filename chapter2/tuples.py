

# tuples are immutable means they cant be changed

a = (1,4,56,567,5678,"manju");
print(type(a));
print(a);
# a[2] = 90 error


a = (1);
print(type(a)) #int because it thinks (1) is integer wrapped in brackets to avoid use (1,)

b = (1,);
print(type(b));



# tuple methods


t = [1,2,3,4,"manju",False,90.6,3];
print(t);
print(t.count(3));   #gives count
print(t.index(3));    #gives index



tuple1 = (1,2,3);
tuple2 = (4,5,6,"manju");
print(tuple1 + tuple2)      #concatination

print(tuple1 * 3);  #can be repeated using *


# checking if exists


a1 = (1,2,3,4,5,6,7);
print(5 in a1);
print(15 in a1);


# unpacking

g = (2,6);
a,b = g;
print(a);
print(b);