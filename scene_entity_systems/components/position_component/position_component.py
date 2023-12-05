from scene_entity_systems.components.component import Component
from vector2d import Vector2D


class PositionComponent(Component):

    position: Vector2D
    transform: Vector2D

    @property
    def x(self):
        return self.position.vector[0]

    @property
    def y(self):
        return self.position.vector[1]
    