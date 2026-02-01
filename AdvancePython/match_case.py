# match-case is a control-flow statement introduced in Python 3.10 that
# allows you to compare a value against multiple patterns and execute the matching block of code.
# It is similar to switch-case in other languages, but more powerful because it supports pattern matching, not just values.

day = 1

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case _:
        print("Invalid day")


def http_status(status: int) -> str:
    match status:
        case 200 | 201:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Invalid Status"


print(http_status(201))


# dictionary merger | union operator

dict1 = {"name": "Adam", "age": 25}
dict2 = {"gender": "Male", "pin": 560061}

new_dict = dict1 | dict2
print(new_dict)
