import random

from scene_entity_systems.components import PhysicsComponent, PhysicsComponentController
from scene_entity_systems.components import PositionComponent, PositionComponentController
from vector2d import Vector2D
from deltaTime import DeltaTime
from random import Random


class PhysicsSystem:

    position_component_controller: PositionComponentController
    delta_time: DeltaTime

    gravity: float = 9.8

    def __init__(self, arg_position_component_controller: PositionComponentController, arg_fixed_delta_time: DeltaTime):
        self.position_component_controller = arg_position_component_controller
        self.delta_time = arg_fixed_delta_time

    def update_physics(self, arg_physics_component: PhysicsComponent):
        self.gravity_update(arg_physics_component)
        self.apply_acceleration(arg_physics_component)
        self.apply_velocity(arg_physics_component)
        self.position_component_controller.iterate_single_component(self.update_transform, arg_physics_component.entity_id, arg_physics_component.velocity)
        self.reset_physics(arg_physics_component)

    def gravity_update(self, arg_physics_component: PhysicsComponent):
        self.apply_force(arg_physics_component, Vector2D(0, self.gravity))

    def update_transform(self, arg_position_component: PositionComponent, arg_velocity: Vector2D):
        arg_position_component.transform += arg_velocity

    def reset_physics(self, arg_physics_component: PhysicsComponent):
        arg_physics_component.transform = Vector2D(0,0)
        arg_physics_component.acceleration = Vector2D(0, 0)

    def apply_velocity(self, arg_physics_component):
        arg_physics_component.transform.vector[0] += arg_physics_component.velocity.vector[0] * self.delta_time.delta_time
        arg_physics_component.transform.vector[1] += arg_physics_component.velocity.vector[1] * self.delta_time.delta_time

    def apply_acceleration(self, arg_physics_component: PhysicsComponent):
        arg_physics_component.velocity.vector[0] += arg_physics_component.acceleration.vector[0] * self.delta_time.delta_time
        arg_physics_component.velocity.vector[1] += arg_physics_component.acceleration.vector[1] * self.delta_time.delta_time

    def apply_force(self, arg_physics_component: PhysicsComponent, arg_force: Vector2D):
        arg_physics_component.acceleration.vector[0] += (arg_force.vector[0] / arg_physics_component.mass)
        arg_physics_component.acceleration.vector[1] += (arg_force.vector[1] / arg_physics_component.mass)





