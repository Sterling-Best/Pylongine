from .meta_component_factory import MetaComponentFactory
from scene_entity_systems.components.component_manager import ComponentManager
from scene_entity_systems.components.component_repository import ComponentRepository
from scene_entity_systems.components.component_controller import ComponentController


class MetaComponentController(ComponentController):

    def __init__(self):
        self.component_factory = MetaComponentFactory()
        self.component_repository = ComponentRepository()
        self.component_manager = ComponentManager()

    def create_meta_component(self) -> int:
        target_entity_id = self.component_factory.component_count
        self.create_component(target_entity_id)
        return target_entity_id



