import time

from deltaTime import DeltaTime

from scene_entity_systems.components import ComponentController
from scene_entity_systems.components.meta_component import MetaComponentFactory
from scene_entity_systems.components.physics_component import PhysicsComponentFactory
from scene_entity_systems.components.position_component import PositionComponentFactory
from scene_entity_systems.components.pygame_render_component import PygameRenderComponentFactory
from scene_entity_systems.systems import PhysicsSystem
from scene_entity_systems.systems import PositionSystem
from scene_entity_systems.systems import PygameRenderSystem

from vector2d import Vector2D

import random


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

    meta_component_controller: ComponentController
    physics_component_controller: ComponentController
    position_component_controller: ComponentController
    pygame_render_component_controller: ComponentController
    physics_system: PhysicsSystem
    position_system: PositionSystem
    pygame_render_system: PygameRenderSystem

    target_frame_rate: int = 60

    def __init__(self):
        self.running = False

        # Initialize timing classes and variables
        self.delta_time = DeltaTime()
        self.fixed_delta_time = DeltaTime()
        self.target_frame_time = 1 / self.target_frame_rate

        # Initialize Component Controller Classes
        self.meta_component_controller = ComponentController(MetaComponentFactory())
        self.physics_component_controller = ComponentController(PhysicsComponentFactory())
        self.position_component_controller = ComponentController(PositionComponentFactory())
        self.pygame_render_component_controller = ComponentController(PygameRenderComponentFactory())

        # Initialize Component System Classes
        self.physics_system = PhysicsSystem(self.position_component_controller, self.fixed_delta_time)
        self.position_system = PositionSystem()
        self.pygame_render_system = PygameRenderSystem(self.position_component_controller)

    def run(self) -> None:
        """
        Main code logic for initializing and looping the environment/scene.

        """
        # Environment Initialization
        self.initialize()
        self.start()
        # Environment Running Loop
        while self.running:
            self.start_update()
            self.update()
            self.fixed_update()
            self.late_update()
            self.render_update()
            self.end_update()
        # Environment End
        self.end()

    def initialize(self):
        self.running = True
        self.setup_delta_time()

    def start(self) -> None:
        for i in range(3):
            self.meta_component_controller.create_component(i)
            self.physics_component_controller.create_component(i)
            self.position_component_controller.create_component(i)
            self.pygame_render_component_controller.create_component(i)
            self.physics_component_controller.iterate_single_component(self.physics_system.apply_force, i, Vector2D(random.random() * 1000, 0))

    def start_update(self):
        self.start_delta_time()

    def update(self):
        pass

    def fixed_update(self):
        while self.fixed_delta_time.get() >= self.target_frame_time:
            self.physics_component_controller.iterate_components(self.physics_system.update_physics)
            self.fixed_delta_time.set(self.fixed_delta_time.get() - self.target_frame_time)

    def late_update(self):
        self.position_component_controller.iterate_components(self.position_system.update_position)

    def render_update(self) -> None:
        self.pygame_render_system.render_background()
        self.pygame_render_component_controller.iterate_components(self.pygame_render_system.render_circle)
        self.pygame_render_system.render_end()

    def end_update(self):
        self.calculate_delta_time()

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
        self.delta_time.set_start_frame(base_start_time)
        if self.fixed_delta_time.get() >= self.target_frame_time:
            self.fixed_delta_time.set_start_frame(base_start_time)

    def calculate_delta_time(self):
        # calculate deltaTime this frame
        end_time = time.time()
        self.delta_time.calculate(end_time)
        self.fixed_delta_time.set(self.fixed_delta_time.delta_time + self.delta_time.get())
