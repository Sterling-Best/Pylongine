from scene_entity_systems.components.component_controller import ComponentController
from .position_component_factory import PositionComponentFactory
from scene_entity_systems.components.component_repository import ComponentRepository
from scene_entity_systems.components.component_manager import ComponentManager


class PositionComponentController(ComponentController):

    def __init__(self):
        self.component_factory = PositionComponentFactory()
        self.component_repository = ComponentRepository()
        self.component_manager = ComponentManager()

