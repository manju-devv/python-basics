# In Python, type definitions describe what kind of data a variable,
# function parameter, or return value is expected to hold.

age: int = 25
name: str = "Manju"
price: float = 99.5
is_active: bool = True


def sum(a: int, b: int) -> int:
    return a + b


print(sum(5, 4))



numbers: list[int] = [1, 2, 3]
names: list[str] = ["A", "B"]

data: dict[str, int] = {"a": 1, "b": 2}
coords: tuple[int, int] = (10, 20)




