from scene_systems.sceneobjectfactory import SceneObjectFactory
from scene_systems.sceneobjectmanager import SceneObjectManager


class SceneObjectController:

    scene_object_factory: SceneObjectFactory
    scene_object_manager: SceneObjectManager

    def __init__(self):
        self.scene_object_factory = SceneObjectFactory()
        self.scene_object_manager = SceneObjectManager()
    