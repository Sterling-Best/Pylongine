from physicscomponentpool import PhysicsComponentPool
from physicscomponent import PhysicsComponent
from typing import Callable

class PhysicsPoolManager:

    _instance = None

    componentPools: dict

    def __new__(cls):
        # Setup for Singleton
        # PhysicsEngine should be singleton
        if cls._instance is None:
            cls._instance = super(PhysicsPoolManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        # "self" attributes for the singleton
        self.componentPools ={}

    def createPool(self, a_poolname: str) -> None:
        self.addPool(PhysicsComponentPool(), a_poolname)

    #TODO: Should you ever add a pool or would it just be created?
    #Should this be public?
    def addPool(self, a_pool: PhysicsComponentPool, a_poolname: str) -> None:
        self.componentPools[a_poolname] = a_pool

    def removePool(self, a_poolname: str) -> None:
        self.componentPools[a_poolname].pop()

    def iteratePools(self, a_callback: Callable) -> None:
        for key, pool in self.componentPools.items():
            pool.iteratePool(a_callback)

    def iterateSpecificPool(self, a_callback: Callable, a_poolname: str) -> None:
        self.componentPools[a_poolname].iteratePool(a_callback)

    def requestCreateComponent(self, x: float = 0, y: float = 0, a_poolname ="Default") -> PhysicsComponent:
        return self.componentPools[a_poolname].createComponent(x, y)




