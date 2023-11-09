from scene_systems.scenemanager import SceneManager
from scene_systems.scene_object_pool_manager import SceneObjectPoolManager


class SceneSystemsFactory:

    def __init__(self):
        pass

    def create_scene_manager(self):
        return SceneManager()

    def create_scene_object_pool_manager(self):
        return SceneObjectPoolManager()

