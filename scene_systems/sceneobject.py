from abc import ABC, abstractmethod

class SceneObject(ABC):

    active = True

    def __init__(self):
        self.active = True

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

