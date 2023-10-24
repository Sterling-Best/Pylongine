from scene_systems.sceneobject import SceneObject

class SceneObjectPool:

    object_pool: list

    def __init__(self) -> None:
        self.object_pool = []

    def add_object(self, a_target_scene_object: SceneObject) -> None:
        self.object_pool.append(a_target_scene_object)

    def remove_object(self, a_target_scene_object: SceneObject) -> None:
        target_index = self.object_pool.index(a_target_scene_object)
        self.object_pool[target_index], self.object_pool[-1] = self.object_pool[-1], self.object_pool[target_index]
        self.object_pool.pop()

    def clear_pool(self):
        self.object_pool = []

    # def create_object(self):
    #     self.add_object(SceneObject())
