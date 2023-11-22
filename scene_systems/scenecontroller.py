
from scene_systems.scenefactory import SceneFactory
from scene_systems.scenemanager import SceneManager
from scene_systems.scenerepository import SceneRepository
from scene_systems.scene import Scene


class SceneController:

    scene_factory: SceneFactory
    scene_manager: SceneManager
    scene_repository: SceneRepository

    def __init__(self):
        self.scene_factory = SceneFactory()
        self.scene_manager = SceneManager()
        self.scene_repository = SceneRepository()

    def add_scene(self, arg_scene_name: str = None) -> None:
        target_scene = self.scene_factory.create_scene(arg_scene_name)
        self.scene_repository.add_scene(target_scene)

    def remove_scene_by_id(self, arg_scene_id: str) -> None:
        self.scene_repository.remove_with_id(arg_scene_id)
        if self.scene_manager.check_active_scenes(arg_scene_id):
            self.scene_manager.deactive_scene(arg_scene_id)

    def remove_scene_by_name(self, arg_scene_name: str) -> None:
        if self.scene_repository.check_for_scene_by_name(arg_scene_name):
            target_scene_id = self.scene_repository.get_scene_id_by_name(arg_scene_name)
            self.remove_scene_by_id(target_scene_id)

    def activate_scene_by_id(self, arg_scene_id: str) -> None:
        if self.scene_repository.check_for_scene_by_id(arg_scene_id):
            self.scene_manager.activate_scene(arg_scene_id)
        else:
            raise ValueError(f"Scene by that id was not found: ID: {arg_scene_id}")

    def activate_scene_by_name(self, arg_scene_name: str) -> None:
        self.scene_manager.activate_scene(self.scene_repository.get_scene_id_by_name(arg_scene_name))

    def deactivate_scene_by_id(self, arg_scene_id: str) -> None:
        if self.scene_repository.check_for_scene_by_id(arg_scene_id):
            self.scene_manager.deactive_scene(arg_scene_id)
        else:
            raise ValueError(f"Scene by that id was not found: ID: {arg_scene_id}")

    def deactivate_scene_by_name(self, arg_scene_name: str) -> None:
        if self.scene_repository.check_for_scene_by_name(arg_scene_name):
            target_scene_id = self.scene_repository.get_scene_id_by_name(arg_scene_name)
            self.scene_manager.deactive_scene(target_scene_id)
        else:
            raise ValueError(f"Scene by that name was not found: ID: {arg_scene_name}")
        
    def get_scene_by_id(self, arg_scene_id: str) -> Scene:
        return self.scene_repository.get_by_id(arg_scene_id)

    def get_scene_by_name(self, arg_scene_name: str) -> Scene:
        return self.scene_repository.get_by_name(arg_scene_name)

    def get_active_scene(self) -> Scene:
        num_of_active_scene_ids = len(self.scene_manager.active_scene_ids)
        if num_of_active_scene_ids > 1:
            raise ValueError(f"There are more the 1 active scene. Please use get_active_scenes_list")
        elif num_of_active_scene_ids == 0:
            target_scene_id = self.scene_manager.active_scene_ids[0]
            return self.scene_repository.get_by_id(target_scene_id)
        else:
            raise ValueError(f"There are no scenes listed in the active scene ID list.")

    def get_active_scenes_list(self) -> list[Scene]:
        if len(self.scene_manager.active_scene_ids) > 0:
            target_scene_list = []
            for scene_id in self.scene_manager.active_scene_ids:
                target_scene_list.append(self.scene_repository.get_by_id(scene_id))
            return target_scene_list
        else:
            raise ValueError(f"There are no scenes listed in the active scene ID list.")


    # TODO: change scene name

    # TODO: clear scene

