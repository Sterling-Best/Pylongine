from scene_entity_systems.components.component import Component
from scene_entity_systems.components.component_factory import ComponentFactory
from .pygame_render_component import PygameRenderComponent
from vector2d import Vector2D


class PygameRenderComponentFactory(ComponentFactory):

    def _setup_component(self, arg_component_count: int, arg_entity_id: int) -> PygameRenderComponent:
        target_render_component: PygameRenderComponent = PygameRenderComponent(arg_component_count, arg_entity_id)
        target_render_component.rgb_red = 100
        target_render_component.rgb_green = 0
        target_render_component.rgb_blue = 0
        target_render_component.draw_type = "circle"
        target_render_component.size = Vector2D(100, 100)
        return target_render_component



