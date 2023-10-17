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

    def fixedUpdate(self):
        pass

    def lateUpdate(self):
        pass

    def renderUpdate(self):
        pass

