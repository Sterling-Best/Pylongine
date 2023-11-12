from scene_systems.scene import Scene

class SceneFactory:

    def __init__(self):
        pass

    def create_scene(self) -> Scene:
        return Scene()

    # TODO: load scene from a file
    def load_from_file(self):
        pass
    