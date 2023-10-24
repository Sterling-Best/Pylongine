from scene_systems.scene import Scene

class SceneManager:

    current_scene: Scene
    scene_pool = dict

    def __init__(self) -> None:
        self.scene_pool = {}

    def new_scene(self, arg_scene_name: str) -> None:
        self.scene_pool[arg_scene_name] = Scene()

    def get_scene(self, arg_scene_name: str) -> Scene:
        return self.scene_pool[arg_scene_name]

    def remove_scene(self, arg_scene_name: str) -> None:
        self.scene_pool.pop(arg_scene_name)

    def load_scene(self, arg_scene_name: str):
        self.scene_pool[arg_scene_name].load_scene()





