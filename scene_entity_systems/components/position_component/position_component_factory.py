from .position_component import PositionComponent
from scene_entity_systems.components.component_factory import ComponentFactory
from vector2d import Vector2D


class PositionComponentFactory(ComponentFactory):

    def _setup_component(self, arg_component_count: int, arg_entity_id: int) -> PositionComponent:
        target_position_component: PositionComponent = PositionComponent(arg_component_count, arg_entity_id)
        target_position_component.position = Vector2D(0, 0)
        target_position_component.transform = Vector2D(0, 0)
        return target_position_component
