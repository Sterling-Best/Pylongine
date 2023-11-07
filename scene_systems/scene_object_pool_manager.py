from scene_systems.sceneobjectpool import SceneObjectPool

class SceneObjectPoolManager:

    scene_object_pools: dict



    def __init__(self) -> None:
        self.scene_object_pools = {}

    def add_pool(self,arg_pool: SceneObjectPool, arg_pool_name: str) -> None:
        self.scene_object_pools[arg_pool_name] = arg_pool

    def remove_pool(self, arg_pool_name: str):
        self.scene_object_pools[arg_pool_name].pop()
