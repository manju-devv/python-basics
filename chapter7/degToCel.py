def f_To_cel(f):
    return (f - 32) * 5 / 9


f = int(input("enter temperature in fahrenheit: "))
c = f_To_cel(f)
print(f"temperature in celsius of {f}°F is: {round(c,2)}°C")
