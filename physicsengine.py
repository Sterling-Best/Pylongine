from physicscomponent import PhysicsComponent

class PhysicsEngine:

    _instance = None

    def __new__(cls):
        #Setup for Singleton
        #PhysicsEngine should be singleton
        if cls._instance is None:
            cls._instance = super(PhysicsEngine, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        # "self" attributes for the singleton

    def update_physics(self, a_target_component: PhysicsComponent):
        a_target_component.position.set_y(a_target_component.position.y + 1)
