from scene_systems.scenemanager import SceneManager
from scene_systems.scene_object_pool_manager import SceneObjectPoolManager
from typing import Callable


class SceneController:

    _instance = None

    scene_manager: SceneManager
    scene_object_pool_manger: SceneObjectPoolManager

    def __new__(cls):
        # Setup for Singleton
        if cls._instance is None:
            cls._instance = super(SceneController, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True

    def initiate_scene(self, arg_scene_name: str):
        pass





