from scene_entity_systems.components import PositionComponent
from vector2d import Vector2D


class PositionSystem:

    def update_position(self, arg_position_component: PositionComponent):
        arg_position_component.position += arg_position_component.transform
        self.reset_transform(arg_position_component)

    def get_position(self, arg_position_component: PositionComponent) -> Vector2D:
        return arg_position_component.position

    def reset_transform(self, arg_position_component: PositionComponent):
        arg_position_component.transform = Vector2D(0, 0)


