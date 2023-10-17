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

    def set_y(self, a_newy: float):
        self.vector[1] = a_newy





