# Operator overloading means giving custom meaning to operators (+, -, *, ==, <, etc.) for user-defined objects (classes).


class Box:
    def __init__(self, value):
        self.value = value

    def __add__(self, num):
        return self.value + num.value


b1 = Box(10)
b2 = Box(20)

print(b1 + b2)





# Operator	Method
# +	      __add__()
# -	      __sub__()
# *	       __mul__()
# /. 	 __truediv__()
# == 	  __eq__()
# <	      __lt__()
# >.    	__gt__()