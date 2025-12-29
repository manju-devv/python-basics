# names = ["Adam", "Tony", "David", "Hulk"]

# name = input("Enter your name: ")
# if name in names:
#     print(f"{name} is present in the list")
# else:
#     print(f"{name} is not present in the list")



num = int(input("Enter marks: "));

match num:
    case n if n <= 100 and n>92:
        print("excellent");
    case n if n <=92 and n > 55:
        print("first class");
    case _:
        print("average");