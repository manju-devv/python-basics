from typing import List, Dict, Optional, Union, Any


# typing Module — Definition

# The typing module provides advanced type definitions that allow
# developers to describe complex data structures, optional values,
# and custom types in Python for static type checking and better code clarity.

# It is mainly used with tools like mypy, IDEs, and linters.


scores: List[int] = [90, 85, 100]
scores.append("90")
print(scores)


user: Dict[str, str] = {"name": "Manju", "city": "Madanapalli"}
user["age"] = 25  # ❌ value is int, expected str
print(user)


# real world example
products: List[Dict[str, int]] = [{"id": 1, "price": 100}, {"id": 2, "price": 200}]
print(products)


# Optional — Very important concept ❗
# 🔹 Definition

# Optional[T] means a value can be either type T OR None.

# Equivalent to:

# T | None   # Python 3.10+


def find(x: int) -> Optional[int]:
    return x if x > 0 else None


print(find(-7))


def parse(value: Union[int, str]) -> int:
    return int(value)


print(parse("6"))


# Any — disable type checking


def log(data: Any) -> None:
    print(data)


print(log([1, 2, 3, 4, 5]))
