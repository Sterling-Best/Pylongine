from abc import ABC, abstractmethod


class SceneObject(ABC):

    active = True

    position_X: float
    position_Y: float

    component_directory: dict

    def __init__(self, arg_pos_x: float = 0, arg_pos_y: float = 0):
        self.active = True
        self.component_directory = {}

    def initialize(self):
        pass

    def start(self):
        pass

    def update(self):
        pass

    def fixed_update(self):
        pass

    def late_update(self):
        pass

    def render_update(self):
        pass

