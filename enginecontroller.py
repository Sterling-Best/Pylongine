import pygame
import sys
import time

from deltaTime import DeltaTime
from physicscontroller import PhysicsController
from physicscomponent import PhysicsComponent

class EngineController:

    target_frame_rate: int = 60

    delta_time: DeltaTime
    fixed_delta_time: DeltaTime

    physics_controller: PhysicsController

    def __init__(self):
        pygame.init()
        self.running = False
        # screen settings
        self.width, self.height = 1280, 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.target_frame_time = 1 / self.target_frame_rate
        self.physics_controller = PhysicsController()
        self.delta_time = DeltaTime()
        self.fixed_delta_time = DeltaTime()
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
            self.start_delta_time()
            #Environment Loop Main logic
            self.update()
            #Fixed
            while self.fixed_delta_time.get() >= self.target_frame_time:
                self.fixed_update()
                self.fixed_delta_time.set(self.fixed_delta_time.get() - self.target_frame_time)
            self.late_update()
            self.render_update()
            self.calculate_delta_time()
        #Exit Environment
        self.end()

    def initialize(self):
        pass

    def start(self) -> None:
        self.running = True
        base_start_time = time.time()
        self.delta_time.set_start_frame(base_start_time)
        self.fixed_delta_time.set_start_frame(base_start_time)
        initialization_time = time.time()
        self.delta_time.calculate(initialization_time)
        self.fixed_delta_time.calculate(initialization_time)
        self.component = self.physics_controller.createComponent(100, 100)

    def update(self):
        pass

    def fixed_update(self):
        self.physics_controller.update_physics()
        self.screen.fill((128, 128, 128))
        pygame.draw.circle(self.screen, (200, 0, 0), (self.component.position.x, self.component.position.y), 50)
        pygame.display.flip()

        #TODO: Apply physics update for physics update simulator here
        #TODO: Apply fixed update for all sceneObjects here

    def late_update(self):
        pass

    def render_update(self) -> None:
        pass

    def end(self):
        pass

    def start_delta_time(self):
        # start keeping track of deltaTime
        base_start_time = time.time()  # calculate time for deltaTime and fixedDelta time so they are sinked
        # print("Base Start Time: " + str(baseStartTime))
        self.delta_time.set_start_frame(base_start_time)
        if self.fixed_delta_time.get() >= self.target_frame_time:
            self.fixed_delta_time.set_start_frame(base_start_time)
            # print("fixedUpdate Loop")
            # print("StartTime " + str(self.fixedDeltaTime.startTime))
            # print("fixedDeltatime " + str(self.fixedDeltaTime.get()))
            # print("DeltaTime " + str(self.deltaTime.get()))
            # print("TargetFrameTime " + str(self.targetFrameTime + baseStartTime))
            # print("New fixedDeltaTime " + str(self.fixedDeltaTime.get() - self.targetFrameTime))

    def calculate_delta_time(self):
        # calculate deltaTime this frame
        end_time = time.time()
        self.delta_time.calculate(end_time)
        self.fixed_delta_time.set(self.fixed_delta_time.delta_time + self.delta_time.get())
        # if self.deltaTime.get() > 0:
        #     print("Main Environment Loop")
        #     print("Fixed Start Time " + str(self.fixedDeltaTime.startTime))
        #     print("fixed Deltatime " + str(self.fixedDeltaTime.deltaTime + self.deltaTime.deltaTime))
        #     print("DeltaTime Start " + str(self.deltaTime.startTime))
        #     print("DeltaTime " + str(self.deltaTime.get()))
        #     print("EndTime " + str(endTime))