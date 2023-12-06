from scene_entity_systems.components import Component


class MetaComponent(Component):

    meta_component_id: int
    scene_entity_id: int
    scene_entity_name: str
    is_active: bool




