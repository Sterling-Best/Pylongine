from typing import Callable

from physicscomponent import PhysicsComponent
from vector2d import Vector2D

class PhysicsComponentPool:

    pool: list = []

    def __init__(self):
        self.pool = []

    def getPool(self) -> list:
        return self.pool

    def addComponent(self, component: PhysicsComponent) -> None:
        self.pool.append(component)

    def removeComponent(self, component: PhysicsComponent) -> None:
        """
        Remove component from pool.

        Using swappable array for optimized removal
        :param component:
        :return:
        """
        targetIndex = self.pool.index(component)
        self.pool[targetIndex], self.pool[-1] = self.pool[-1], self.pool[targetIndex]
        self.pool.pop()

    def createComponent(self, x: float = 0, y: float = 0) -> None:
        newComponent= PhysicsComponent(Vector2D([x, y]))
        self.addComponent(newComponent)
        return newComponent

    def iteratePool(self, a_callback: Callable):
        for component in self.pool:
            a_callback(component)






