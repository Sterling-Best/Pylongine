from physicsengine import PhysicsEngine
from physicspoolmanager import PhysicsPoolManager
from physicscomponentpool import PhysicsComponentPool
from physicscomponent import PhysicsComponent

class PhysicsController:

    _instance = None

    physics_engine: PhysicsEngine
    physics_pool_manager: PhysicsPoolManager

    def __new__(cls):
        # Setup for Singleton
        if cls._instance is None:
            cls._instance = super(PhysicsController, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        #Class Variables
        self.physics_engine = PhysicsEngine()
        self.physics_pool_manager = PhysicsPoolManager()
        self.setup()

    def setup(self):
        self.physics_pool_manager.create_pool("default")

    def update_physics(self):
        self.physics_pool_manager.iterate_pools(self.physics_engine.update_physics)

    def update_specific_physics(self, a_physics_pool_name: str):
        self.physics_pool_manager.iterate_specific_pool(self.physics_engine.update_physics(), a_physics_pool_name)

    def create_component(self, x: float = 0, y: float = 0, a_pool_name: str = "default") -> PhysicsComponent:
        return self.physics_pool_manager.request_create_component(x, y, a_pool_name)










