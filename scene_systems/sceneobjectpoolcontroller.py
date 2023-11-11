from scene_systems.sceneobjectpoolfactory import SceneObjectPoolFactory
from scene_systems.sceneobjectpoolmanager import SceneObjectPoolManager
from scene_systems.sceneobjectpoolrepository import SceneObjectPoolRepository


class SceneObjectPoolController:

    scene_object_pool_factory: SceneObjectPoolFactory
    scene_object_pool_manager: SceneObjectPoolManager
    scene_object_pool_repository: SceneObjectPoolRepository

    def __init__(self):
        self.scene_object_pool_factory = SceneObjectPoolFactory()
        self.scene_object_pool_manager = SceneObjectPoolManager()
        self.scene_object_pool_repository = SceneObjectPoolRepository()