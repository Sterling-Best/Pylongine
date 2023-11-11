from scene_systems.scene import Scene
from scene_systems.sceneobjectpoolmanager import SceneObjectPoolManager
from typing import Callable


class SceneManager:

    # Class Variables
    current_scene: Scene
    scene_pool = dict

    def __init__(self):
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







