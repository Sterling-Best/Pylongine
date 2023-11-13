from abc import ABC, abstractmethod


class Scene(ABC):
    """
    Parent Class for a scene in python.

    """

    scene_name: str
    scene_id: str
    scene_object_pool_ids: list[str]

    def __init__(self, arg_scene_id: str, arg_scene_name: str = None):
        self.scene_id = arg_scene_id
        if arg_scene_name is None:
            self.scene_name = arg_scene_id
        else:
            self.scene_name = arg_scene_name

    def change_scene_name(self, arg_scene_name: str) -> None:
        self.scene_name = arg_scene_name

    def add_pool_id(self, arg_scene_object_pool_id: str) -> None:
        if arg_scene_object_pool_id not in self.scene_object_pool_ids:
            self.scene_object_pool_ids.append(arg_scene_object_pool_id)
        else:
            raise ValueError(
                f"ID ({arg_scene_object_pool_id}, already listed with current scene {self.scene_name}, {self.scene_id}.")

    def remove_pool_id(self, arg_scene_object_pool_id: str) -> None:
        self.scene_object_pool_ids.remove(arg_scene_object_pool_id)

    @abstractmethod
    def scene_configuration(self):
        pass
