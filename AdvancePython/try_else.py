
# else is executed only if try is successful


try:
    a = int(input("enter a number: "))
    print(a)
except Exception as e:
    print(e)
else:
    print("since try executed its in else block")
