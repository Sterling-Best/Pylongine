from vector2d import Vector2D
from scene_entity_systems.components.component import Component


class PhysicsComponent(Component):

    transform: Vector2D
    velocity: Vector2D
    acceleration: Vector2D
    mass: float
