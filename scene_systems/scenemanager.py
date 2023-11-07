from scene_systems.scene import Scene
from scene_systems.scene_object_pool_manager import SceneObjectPoolManager
from typing import Callable


class SceneManager:

    # Singleton Variables
    _instance = None

    # Class Variables
    current_scene: Scene
    scene_pool = dict

    def __new__(cls):
        # Setup for Singleton
        # PhysicsEngine should be singleton
        if cls._instance is None:
            cls._instance = super(SceneManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self.scene_pool = {}

    def new_scene(self, arg_scene_name: str) -> None:
        self.scene_pool[arg_scene_name] = Scene()

    def get_scene(self, arg_scene_name: str) -> Scene:
        return self.scene_pool[arg_scene_name]

    def get_current_scene(self) -> Scene:
        return self.current_scene

    def remove_scene(self, arg_scene_name: str) -> None:
        self.scene_pool.pop(arg_scene_name)

    def load_scene(self, arg_scene_name: str) -> None:
        self.current_scene = self.scene_pool[arg_scene_name]
        self.current_scene.load_scene()







