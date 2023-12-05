from scene_entity_systems.components.component import Component
from vector2d import Vector2D


class PygameRenderComponent(Component):

    rgb_red: int
    rgb_green: int
    rgb_blue: int
    draw_type: str
    size: Vector2D
