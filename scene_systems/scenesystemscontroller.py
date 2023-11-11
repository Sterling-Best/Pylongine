from scene_systems.scenecontroller import SceneController
from scene_systems.sceneobjectpoolcontroller import SceneObjectPoolController
from scene_systems.sceneobjectcontroller import SceneObjectController


class SceneSystemsController:

    scene_controller: SceneController
    scene_object_pool_controller: SceneObjectPoolController
    scene_object_controller: SceneObjectController

    def __init__(self):
        self.scene_controller = SceneController()
        self.scene_object_pool_controller = SceneObjectPoolController()
        self.scene_object_controller = SceneObjectController()