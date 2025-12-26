# dictionaries used to store keyvalue pairs

details = {
    "name": "manju",
    "marks": 42,
    "isQualified": True,
    "list": [1, 2, 3],
    "tuple": (1, 2, 3),
}

print(details)
print(type(details))

print(details["name"])
# print(details[1])
# error because index only works with list and tuples

print(details["list"]);




# dictionaries are mutable
# they are unordered
# cannot contain duplicate keys 
# they are indexed