from scene_systems.scene import Scene


class SceneManager:

    # TODO: should the active scene be in manager or repository?
    # Class Variables
    active_scene_ids: list[str]

    def __init__(self):
        pass

    def activate_scene(self, arg_scene_id: str) -> None:
        self.active_scene_ids.append(arg_scene_id)

    def deactive_scene(self, arg_scene_id: str) -> None:
        if self.check_active_scenes(arg_scene_id):
            self.active_scene_ids.remove(arg_scene_id)
        else:
            raise ValueError(f"Scene by that id was not found: ID: {arg_scene_id}")

    def get_active_scenes(self) -> list[str]:
        return self.active_scene_ids

    def check_active_scenes(self, arg_scene_id: str) -> bool:
        return arg_scene_id in self.active_scene_ids

    def rename_scene(self, arg_target_scene: Scene, arg_scene_name) -> None:
        arg_target_scene.change_scene_name(arg_scene_name)









