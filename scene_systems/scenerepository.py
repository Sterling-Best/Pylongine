from scene_systems.scene import Scene


class SceneRepository:

    scene_by_id: dict[str, Scene]
    scene_by_name: dict[str, list[str]]

    def __init__(self):
        self.scene_by_id = {}
        self.scene_by_name = {}

    def get_by_id(self, arg_scene_id: str) -> Scene:
        return self.scene_by_id[arg_scene_id]

    def get_by_name(self, arg_scene_name: str) -> Scene:
        if len(self.scene_by_name[arg_scene_name]) > 1:
            raise ValueError(f"Too Scenes of the same name: Key: {arg_scene_name}, Values: {self.scene_by_name[arg_scene_name]}")
        else:
            return self.scene_by_id[self.scene_by_name[arg_scene_name][0]]

    def get_scene_id_by_name(self, arg_scene_name: str) -> str:
        if len(self.scene_by_name[arg_scene_name]) > 1:
            raise ValueError(f"Too Scenes of the same name: Key: {arg_scene_name}, Values: {self.scene_by_name[arg_scene_name]}")
        else:
            return self.scene_by_name[arg_scene_name][0]

    def check_for_scene_by_id(self, arg_scene_id: str) -> bool:
        if arg_scene_id in self.scene_by_id.keys():
            return True
        else:
            return False

    def check_for_scene_by_name(self, arg_scene_name: str) -> bool:
        if arg_scene_name in self.scene_by_name.keys():
            if len(self.scene_by_name[arg_scene_name]) > 1:
                raise ValueError(
                    f"Too Scenes of the same name: Key: {arg_scene_name}, Values: {self.scene_by_name[arg_scene_name]}")
            else:
                return True
        else:
            return False

    def add_scene(self, arg_target_scene: Scene) -> None:
        self.scene_by_id[arg_target_scene.scene_id] = arg_target_scene
        if arg_target_scene.scene_name not in self.scene_by_name.keys():
            self.scene_by_name[arg_target_scene.scene_name] = []
            self.scene_by_name[arg_target_scene.scene_name].append(arg_target_scene.scene_id)
        else:
            self.scene_by_name[arg_target_scene.scene_name].append(arg_target_scene.scene_id)

    def remove_with_id(self, arg_scene_id: str) -> None:
        if self.check_for_scene_by_id(arg_scene_id):
            target_scene_name = self.get_by_id(arg_scene_id).scene_name
            if len(self.scene_by_name[target_scene_name]) > 1:
                self.scene_by_name[target_scene_name].remove(arg_scene_id)
            else:
                del self.scene_by_name[target_scene_name]
            del self.scene_by_id[arg_scene_id]
        else:
            raise ValueError(f"Scene by that id was not found: ID: {arg_scene_id}")


    def remove_with_name(self, arg_scene_name: str) -> None:
        if self.check_for_scene_by_name(arg_scene_name):
            if len(self.scene_by_name[arg_scene_name]) > 1:
                raise ValueError(f"Too Scenes of the same name: Key: {arg_scene_name}, Values: {self.scene_by_name[arg_scene_name]}")
            else:
                self.remove_with_id(self.scene_by_name[arg_scene_name][0])
        else:
            raise ValueError(f"Scene by that name was not found: Name: {arg_scene_name}")


    def clear_scenes(self) -> None:
        self.scene_by_name.clear()
        self.scene_by_id.clear()




