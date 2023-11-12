from abc import ABC, abstractmethod

from scene_systems.sceneobjectpool import SceneObjectPool
from scene_systems.sceneobject import SceneObject
class Scene(ABC):
    """
    Parent Class for a scene in python.

    Scenes need to contain all the data
    """
    scene_object_pool: SceneObjectPool

    scene_name: str
    scene_id: str

    def __init__(self, arg_scene_id: str, arg_scene_name: str = None):
        self.scene_id = arg_scene_id
        if arg_scene_name == None:
            self.scene_name = arg_scene_id
        else:
            self.scene_name = arg_scene_name

    @abstractmethod
    def setup_scene(self):
        pass

    def load_scene(self):
        pass
