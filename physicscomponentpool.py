from typing import Callable

from physicscomponent import PhysicsComponent
from vector2d import Vector2D

class PhysicsComponentPool:

    pool: list = []

    def __init__(self):
        self.pool = []

    def get_pool(self) -> list:
        return self.pool

    def add_component(self, component: PhysicsComponent) -> None:
        self.pool.append(component)

    def remove_component(self, component: PhysicsComponent) -> None:
        """
        Remove component from pool.

        Using swappable array for optimized removal
        :param component:
        :return:
        """
        target_index = self.pool.index(component)
        self.pool[target_index], self.pool[-1] = self.pool[-1], self.pool[target_index]
        self.pool.pop()

    def create_component(self, x: float = 0, y: float = 0) -> None:
        new_component = PhysicsComponent(Vector2D([x, y]))
        self.add_component(new_component)
        return new_component

    def iterate_pool(self, a_callback: Callable):
        for component in self.pool:
            a_callback(component)






