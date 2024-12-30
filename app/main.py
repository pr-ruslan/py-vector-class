from typing import Any
from math import sqrt


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Any) -> Any:
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y
        )

    def __sub__(self, other: Any) -> Any:
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y
        )

    def __mul__(self, other: Any) -> Any:
        if isinstance(other, float):
            return Vector(
                x=self.x * other,
                y=self.y * other
            )
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple) -> Any:
        return Vector(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return sqrt(self.x**2 + self.y**2)

    def get_normalized(self, other: Any) -> Any:
        pass

    def angle_between(self):
        pass

    def get_angle(self):
        pass