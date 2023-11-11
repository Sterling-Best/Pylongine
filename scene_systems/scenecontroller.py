
from scene_systems.scenefactory import SceneFactory
from scene_systems.scenemanager import SceneManager
from scene_systems.scenerepository import SceneRepository


class SceneController:

    scene_factory: SceneFactory
    scene_manager: SceneManager
    scene_repository: SceneRepository

    def __init__(self):
        self.scene_factory = SceneFactory()
        self.scene_manager = SceneManager()
        self.scene_repository = SceneRepository()
