from dataclasses import dataclass, field
import numpy

@dataclass
class Vector2D:

    vector: list[float]

    def __init__(self, arg_x: float, arg_y: float):
        self.vector = [arg_x, arg_y]

    @property
    def x(self) -> float:
        return self.vector[0]

    @property
    def y(self) -> float:
        return self.vector[1]

    def set(self, a_new_x: float, a_new_y: float):
        self.vector[0], self.vector[1] = a_new_x, a_new_y

    def set_x(self, a_new_x: float):
        self.vector[0] = a_new_x

    def set_y(self, a_new_y: float):
        self.vector[1] = a_new_y

    def __add__(self, other):
        target_vector: Vector2D = Vector2D(0, 0)
        target_vector.vector[0] = self.vector[0] + other.vector[0]
        target_vector.vector[1] = self.vector[1] + other.vector[1]
        return target_vector
