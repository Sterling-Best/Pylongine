from .meta_component import MetaComponent
from scene_entity_systems.components.component_factory import ComponentFactory


class MetaComponentFactory(ComponentFactory):

    meta_component_str: str = "MTC"

    def _setup_component(self, arg_component_id: int, arg_entity_id: int) -> MetaComponent:
        target_meta_component: MetaComponent = MetaComponent(arg_component_id, arg_component_id)
        target_meta_component.scene_entity_name = self.generate_entity_name(arg_entity_id)
        return target_meta_component

    def generate_entity_name(self, arg_entity_id: int) -> str:
        return self.meta_component_str + "-" + str(arg_entity_id)





