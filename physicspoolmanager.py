from physicscomponentpool import PhysicsComponentPool
from physicscomponent import PhysicsComponent
from typing import Callable

class PhysicsPoolManager:

    _instance = None

    component_pools: dict

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
        self.component_pools ={}

    def create_pool(self, a_pool_name: str) -> None:
        self.add_pool(PhysicsComponentPool(), a_pool_name)

    #TODO: Should you ever add a pool or would it just be created?
    #Should this be public?
    def add_pool(self, a_pool: PhysicsComponentPool, a_pool_name: str) -> None:
        self.component_pools[a_pool_name] = a_pool

    def remove_pool(self, a_pool_name: str) -> None:
        self.component_pools[a_pool_name].pop()

    def iterate_pools(self, a_callback: Callable) -> None:
        for key, pool in self.component_pools.items():
            pool.iterate_pool(a_callback)

    def iterate_specific_pool(self, a_callback: Callable, a_pool_name: str) -> None:
        self.component_pools[a_pool_name].iterate_pool(a_callback)

    def request_create_component(self, x: float = 0, y: float = 0, a_pool_name ="Default") -> PhysicsComponent:
        return self.component_pools[a_pool_name].create_component(x, y)
