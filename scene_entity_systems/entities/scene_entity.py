from scene_entity_systems.components import Component


class SceneEntity:

    entity_id: int
    entity_components: dict[str, Component]
