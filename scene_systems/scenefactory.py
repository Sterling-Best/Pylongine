from scene_systems.scene import Scene
from engine_tools.uniqueidgenerator import UniqueIDGenerator

class SceneFactory:

    scene_id_generator: UniqueIDGenerator

    def __init__(self):
        self.scene_id_generator = UniqueIDGenerator("SCN")

    def create_scene(self, arg_scene_name: str = None) -> Scene:
        target_scene = Scene(self.scene_id_generator.generate_id(), arg_scene_name)
        return target_scene

    # TODO: load scene from a file
    def load_from_file(self):
        pass
    