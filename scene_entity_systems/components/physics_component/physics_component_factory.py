from .physics_component import PhysicsComponent
from vector2d import Vector2D
from scene_entity_systems.components.component_factory import ComponentFactory


class PhysicsComponentFactory(ComponentFactory):

    def _setup_component(self, arg_component_count: int, arg_entity_id: int) -> PhysicsComponent:
        target_physics_component: PhysicsComponent = PhysicsComponent(arg_component_count, arg_entity_id)
        target_physics_component.transform = Vector2D(0, 0)
        target_physics_component.velocity = Vector2D(0, 0)
        target_physics_component.acceleration = Vector2D(0, 0)
        target_physics_component.mass = 1
        return target_physics_component


