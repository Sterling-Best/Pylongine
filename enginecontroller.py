import pygame
import sys
import time

from deltaTime import DeltaTime
from physicscontroller import PhysicsController
from physicscomponent import PhysicsComponent

class EngineController:
    """
    EngineController

    Manages the main logic stages for the engine as well as manage the setup of controller/manager classes and
    interactions.

    This class is responsible for initiating the program and runtime environment, operating the main game loop (and its
    stages various stages including update(), fixed_update(), and late_update()) and the engine's time references. Main
    section of the code focuses on the run() method that initializes the engine with the initialize() and start()
    methods. Then while self.running is true calls update(), fixed_update() and late_update() to run the code. Physics
    will run in fixed_update() at the desired target_frame_rate regardless of what the timing for each loop/frame of
    the engine.


    Attributes:
        delta_time (DeltaTime): instance for calculating the time each loop/frame takes. Works at the begging and end
        of the frame loop.
        fixed_delta_time (DeltaTime): instance for calculating the time between each fixed_update
        physics_controller (PhysicsController): General controller for engine Physics, deals with initiating and running
        the physics, as well as interactions between the physics sub-systems and requests from other classes.
        target_frame_rate (int): used to indicate the desired frame rate. Used to calculate the frame timings. Used
        particularly with fixed_update().

    """

    delta_time: DeltaTime
    fixed_delta_time: DeltaTime
    physics_controller: PhysicsController

    target_frame_rate: int = 60

    def __init__(self):
        pygame.init()
        self.running = False
        #Initiate Main Classes
        self.physics_controller = PhysicsController()
        self.delta_time = DeltaTime()
        self.fixed_delta_time = DeltaTime()
        # screen settings
        self.width, self.height = 1280, 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.target_frame_time = 1 / self.target_frame_rate
        #Test Cases
        self.component = PhysicsComponent()

    def run(self) -> None:
        """
        Main code logic for initializing and looping the environment/scene.

        """
        #Environment Initialization
        self.initialize()
        self.start()
        #Environment Running Loop
        while self.running:
            #Start loop
            self.start_delta_time() #Always get time at start of loop
            #Environment Loop Main logic
            self.update()
            #Fixed
            while self.fixed_delta_time.get() >= self.target_frame_time:
                self.fixed_update()
                self.fixed_delta_time.set(self.fixed_delta_time.get() - self.target_frame_time)
            self.late_update()
            self.render_update()
            #End Loop
            self.calculate_delta_time() #Always calculate delta_time at end of loop
        #Exit Environment
        self.end()

    def initialize(self):
        pass

    def start(self) -> None:
        self.running = True
        self.setup_delta_time()
        #Test
        self.component = self.physics_controller.create_component(100, 100)

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

    def setup_delta_time(self) -> None:
        base_start_time = time.time()
        self.delta_time.set_start_frame(base_start_time)
        self.fixed_delta_time.set_start_frame(base_start_time)
        initialization_time = time.time()
        self.delta_time.calculate(initialization_time)
        self.fixed_delta_time.calculate(initialization_time)

    def start_delta_time(self):
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
