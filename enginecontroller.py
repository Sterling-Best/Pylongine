import pygame
import sys
import time

from deltaTime import DeltaTime
from physicscontroller import PhysicsController
from physicscomponent import PhysicsComponent

class EngineController:

    targetFrameRate: int = 60

    deltaTime: DeltaTime
    fixedDeltaTime: DeltaTime

    physicsController: PhysicsController

    def __init__(self):
        pygame.init()
        self.running = False
        # screen settings
        self.width, self.height = 1280, 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.targetFrameTime = 1 / self.targetFrameRate
        self.physicsController = PhysicsController()
        self.deltaTime = DeltaTime()
        self.fixedDeltaTime = DeltaTime()
        self.component = PhysicsComponent()

    def run(self) -> None:
        """
        EngineController.run()

        Main code logic for initializing and looping the environment/scene.

        """
        #Environment Initialization
        self.initialize()
        self.start()
        #Environment Running Loop
        while self.running:
            self.startDeltaTime()
            #Environment Loop Main logic
            self.update()
            #Fixed
            while self.fixedDeltaTime.get() >= self.targetFrameTime:
                self.fixedUpdate()
                self.fixedDeltaTime.set(self.fixedDeltaTime.get() - self.targetFrameTime)
            self.lateUpdate()
            self.renderUpdate()
            self.calculateDeltaTime()
        #Exit Environment
        self.end()

    def initialize(self):
        pass

    def start(self) -> None:
        self.running = True
        baseStartTime = time.time()
        self.deltaTime.setStartFrame(baseStartTime)
        self.fixedDeltaTime.setStartFrame(baseStartTime)
        initializationTime = time.time()
        self.deltaTime.calculate(initializationTime)
        self.fixedDeltaTime.calculate(initializationTime)
        self.component = self.physicsController.createComponent(100, 100)

    def update(self):
        pass

    def fixedUpdate(self):
        self.physicsController.updatePhysics()
        self.screen.fill((128, 128, 128))
        pygame.draw.circle(self.screen, (200, 0, 0), (self.component.position.x, self.component.position.y), 50)
        pygame.display.flip()

        #TODO: Apply physics update for physics update simulator here
        #TODO: Apply fixed update for all sceneObjects here

    def lateUpdate(self):
        pass

    def renderUpdate(self) -> None:
        pass

    def end(self):
        pass

    def startDeltaTime(self):
        # start keeping track of deltaTime
        baseStartTime = time.time()  # calculate time for deltaTime and fixedDelta time so they are sinked
        # print("Base Start Time: " + str(baseStartTime))
        self.deltaTime.setStartFrame(baseStartTime)
        if self.fixedDeltaTime.get() >= self.targetFrameTime:
            self.fixedDeltaTime.setStartFrame(baseStartTime)
            # print("fixedUpdate Loop")
            # print("StartTime " + str(self.fixedDeltaTime.startTime))
            # print("fixedDeltatime " + str(self.fixedDeltaTime.get()))
            # print("DeltaTime " + str(self.deltaTime.get()))
            # print("TargetFrameTime " + str(self.targetFrameTime + baseStartTime))
            # print("New fixedDeltaTime " + str(self.fixedDeltaTime.get() - self.targetFrameTime))

    def calculateDeltaTime(self):
        # calculate deltaTime this frame
        endTime = time.time()
        self.deltaTime.calculate(endTime)
        self.fixedDeltaTime.set(self.fixedDeltaTime.deltaTime + self.deltaTime.get())
        # if self.deltaTime.get() > 0:
        #     print("Main Environment Loop")
        #     print("Fixed Start Time " + str(self.fixedDeltaTime.startTime))
        #     print("fixed Deltatime " + str(self.fixedDeltaTime.deltaTime + self.deltaTime.deltaTime))
        #     print("DeltaTime Start " + str(self.deltaTime.startTime))
        #     print("DeltaTime " + str(self.deltaTime.get()))
        #     print("EndTime " + str(endTime))