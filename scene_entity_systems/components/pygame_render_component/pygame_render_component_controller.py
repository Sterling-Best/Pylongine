from scene_entity_systems.components.component_controller import ComponentController
from scene_entity_systems.components.component_repository import ComponentRepository
from scene_entity_systems.components.component_manager import ComponentManager
from .pygame_render_component_factory import PygameRenderComponentFactory


class PygameRenderComponentController(ComponentController):

    def __init__(self):
        self.component_factory = PygameRenderComponentFactory()
        self.component_repository = ComponentRepository()
        self.component_manager = ComponentManager()
