from abc import ABC, abstractmethod
class Scene(ABC):
    """
    Parent Class for a scene in python.

    Scenes need to contain all the data
    """

    def __init__(self):
        pass

    @abstractmethod
    def setup_scene(self):
        pass

    def add_object(self):
        pass

    def remove_object(self):
        pass




