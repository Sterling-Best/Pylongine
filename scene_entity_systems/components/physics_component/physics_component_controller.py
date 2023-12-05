from scene_entity_systems.components.component_controller import ComponentController
from .physics_component_factory import PhysicsComponentFactory
from scene_entity_systems.components.component_repository import ComponentRepository
from scene_entity_systems.components.component_manager import ComponentManager


class PhysicsComponentController(ComponentController):

    def __init__(self):
        self.component_factory = PhysicsComponentFactory()
        self.component_repository = ComponentRepository()
        self.component_manager = ComponentManager()
        