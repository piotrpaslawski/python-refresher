import math
from typing import Self, Union

class Point:
    # Constructor - initalizing the point
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # String representation of the point
    def __str__(self) -> str:
        return f"(X={self.x}, Y={self.y})"

    # Detailed string representation
    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def __call__(self) -> tuple:
        return (self.x, self.y)

    # Returning the coordinates of the point as list element
    def __getitem__(self, index: int) -> Union[int, float]:
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Index out of range")

    # Setting the coordinates of the point as list element
    def __setitem__(self, index: int, coordinate: Union[int, float]) -> Union[int, float]:
        if index == 0:
            self.x = coordinate
        elif index == 1:
            self.y = coordinate
        else:
            raise IndexError("Index out of range")

    # Changing the sign of the coordinates
    def __neg__(self) -> Self:
        return Point(-self.x, -self.y)

    # Adding two points
    def __add__(self, other: Self) -> Self:
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    # Substracting two points
    def __sub__(self, other: Self) -> Self:
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        return NotImplemented

    # Multiplying a point by a number
    def __mul__(self, value: Union[int, float]) -> Self:
        return Point(self.x * value, self.y * value)

    # Dividing a point by a number
    def __truediv__(self, value: Union[int, float]) -> Self:
        return Point(self.x / value, self.y / value)

    # Checking if points are equal
    def __eq__(self, other: Self) -> bool:
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    # Checking if points are different
    def __ne__(self, other: Self) -> bool:
        return not self == other

    # Distance from the origin
    def __abs__(self) -> float:
        return self.x ** 2 + self.y ** 2

    # Check if a point's distance from the origin is smaller than another's
    def __lt__(self, other: Self) -> bool:
        if isinstance(other, Point):
            return (self.x ** 2 + self.y ** 2) < (other.x ** 2 + other.y ** 2)
        return NotImplemented

    # Check if a point's distance from the origin is bigger than another's
    def __gt__(self, other: Self) -> bool:
        if isinstance(other, Point):
            return (self.x ** 2 + self.y ** 2) > (other.x ** 2 + other.y ** 2)
        return NotImplemented

    # Rounding to a specified number of decimal places
    def __round__(self, digits: int = 0) -> Self:
        return Point(round(self.x, digits), round(self.y, digits))

    # Truncating the mantissa
    def __trunc__(self) -> Self:
        return Point(int(self.x), int(self.y))

p1 = Point(10.1, 15.9)
p2 = Point(3.4, 2.6)

print(f"Point A: {repr(p1)}")
print(f"It means that coordinates are {p1}")
print(f"Reflection of the point A through the origin: {-p1}")
print(f"Point B: X coordinate is {p2[0]}, Y coordinate is {p2[1]}")
print(f"Let's change Y coordinate of A point to 12.")
p1[1] = 12.8
print(f"Point A{p1}\n")

print(f"Sum of coordinates A and B: {p1 + p2}")
print(f"Substraction of coordinates A and B: {p1 - p2}")
print(f"Multiplying point A by a 5: {p1 * 5}")
print(f"Dividing point A by a 5: {p1 / 5}\n")

print(f"Distance from the origin of point A: {abs(p1)}")
print(f"Are points equal? {p1 == p2}")
print(f"Are points different? {p1 != p2}")
print(f"Is point A closer than B to origin? {p1 < p2}")
print(f"Is point A further than B to origin? {p1 > p2}")

print(f"Rounding coordinates of A point: {round(p1)}")
print(f"Truncating coordinates of A point: {math.trunc(p1)}")
