from abc import ABC, abstractmethod

from sceneobjectpool import SceneObjectPool
from sceneobject import SceneObject
class Scene(ABC):
    """
    Parent Class for a scene in python.

    Scenes need to contain all the data
    """
    scene_object_pool: SceneObjectPool

    scene_name: str

    def __init__(self):
        self.scene_object_pool = SceneObjectPool()

    @abstractmethod
    def setup_scene(self):
        pass

    def add_object(self, arg_target_scene_object: SceneObject):
        self.scene_object_pool.add_object(arg_target_scene_object)

    def remove_object(self, arg_target_scene_object: SceneObject):
        self.scene_object_pool.remove_object(arg_target_scene_object)
