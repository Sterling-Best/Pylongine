from scene_systems.scene import Scene


class SceneRepository:

    scene_by_id: dict[str, Scene]
    scene_by_name: dict[str, list[str]]

    def __init__(self):
        self.scene_by_id = {}
        self.scene_by_name = {}

    def add_scene(self, arg_target_scene: Scene) -> None:
        self.scene_by_id[arg_target_scene.scene_id] = arg_target_scene
        if arg_target_scene.scene_name not in self.scene_by_name.keys():
            self.scene_by_name[arg_target_scene.scene_name] = []
            self.scene_by_name[arg_target_scene.scene_name].append(arg_target_scene.scene_id)
        else:
            self.scene_by_name[arg_target_scene.scene_name].append(arg_target_scene.scene_id)

    def remove_with_id(self, arg_scene_id: str) -> None:
        target_scene_name = self.get_by_id(arg_scene_id).scene_name
        if len(self.scene_by_name[target_scene_name]) > 1:
            self.scene_by_name[target_scene_name].remove(arg_scene_id)
        else:
            del self.scene_by_name[target_scene_name]
        del self.scene_by_id[arg_scene_id]

    def remove_with_name(self, arg_scene_name: str) -> None:
        if len(self.scene_by_name[arg_scene_name]) > 1:
            raise ValueError(f"Too Scenes of the same name: Key: {arg_scene_name}, Value: {self.scene_by_name[arg_scene_name]}")
        else:
            self.remove_with_id(self.scene_by_name[arg_scene_name][0])

    def get_by_id(self, arg_scene_id) -> Scene:
        return self.scene_by_id[arg_scene_id]

    def get_by_name(self, arg_scene_name) -> Scene:
        if len(self.scene_by_name[arg_scene_name]) > 1:
            raise ValueError(f"Too Scenes of the same name: Key: {arg_scene_name}, Value: {self.scene_by_name[arg_scene_name]}")
        else:
            return self.scene_by_id[self.scene_by_name[arg_scene_name][0]]

    def clear_scenes(self) -> None:
        self.scene_by_name.clear()
        self.scene_by_id.clear()




