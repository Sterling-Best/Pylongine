from physicsengine import PhysicsEngine
from physicspoolmanager import PhysicsPoolManager
from physicscomponentpool import PhysicsComponentPool
from physicscomponent import PhysicsComponent

class PhysicsController:

    _instance = None

    physicsEngine: PhysicsEngine
    physicsPoolManager: PhysicsPoolManager

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
        self.physicsEngine = PhysicsEngine()
        self.physicsPoolManager = PhysicsPoolManager()
        self.setup()

    def setup(self):
        self.physicsPoolManager.createPool("default")

    def updatePhysics(self):
        self.physicsPoolManager.iteratePools(self.physicsEngine.updatePhysics)

    def updateSpecificPhysics(self, a_physicsPoolName: str):
        self.physicsPoolManager.iterateSpecificPool(self.physicsEngine.updatePhysics(), a_physicsPoolName)

    def createComponent(self, x: float = 0, y: float = 0, a_poolname: str = "default") -> PhysicsComponent:
        return self.physicsPoolManager.requestCreateComponent(x, y, a_poolname)










