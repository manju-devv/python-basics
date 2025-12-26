details = {
    "name": "manju",
    "marks": 42,
    "isQualified": True,
    "list": [1, 2, 3],
    "tuple": (1, 2, 3),
    0: "anime",
}


# print(details.items()); #returns in form of tuples
# print(details.keys());
# print(details.values());

# details.update({"marks": 41,"role": "sutudent"});    #if the key is matched it updates else record is created;


# print(details);

# print(details.get("age", 0))    # default value
# print(details.get("name3"));  #this returns none if not found
# print(details["name3"]);       #this returns err if not found



for key, value in details.items():
    print(key, value)


# details["city"] = "banglore";
# print(details);

# newDict = details.pop("marks");
# print(newDict);


# popitem()
# Removes last inserted item

# details.popitem();
# print(details);



# clear()
# Removes everything


# details.clear()
# print(details);



# copy()
# Creates a shallow copy
new_details = details.copy();

print(details);
print(new_details);



squares = {x: x*x for x in range(10)}
print(squares)
