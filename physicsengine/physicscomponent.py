from dataclasses import dataclass, field
from vector2d import Vector2D

@dataclass
class PhysicsComponent:

    position: Vector2D = field(default_factory=lambda: Vector2D())
    velocity: Vector2D = field(default_factory=lambda: Vector2D())
    acceleration: Vector2D = field(default_factory=lambda: Vector2D())
    mass: float = field(default_factory=lambda: 1.0)











