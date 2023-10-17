from dataclasses import dataclass, field
import numpy

@dataclass
class Vector2D:

    vector: numpy.ndarray = field(default_factory=lambda: numpy.array([0, 0]))

    @property
    def x(self):
        return self.vector[0]

    @property
    def y(self):
        return self.vector[1]

    def set(self, a_new_x: float, a_new_y: float):
        self.vector[0], self.vector[1] = a_new_x, a_new_y

    def set_x(self, a_new_x: float):
        self.vector[0] = a_new_x

    def set_y(self, a_new_y: float):
        self.vector[1] = a_new_y







