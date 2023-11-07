from scene_systems.scenemanager import SceneManager
from typing import Callable


class SceneController:

    _instance = None

    def __new__(cls):
        # Setup for Singleton
        # PhysicsEngine should be singleton
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




