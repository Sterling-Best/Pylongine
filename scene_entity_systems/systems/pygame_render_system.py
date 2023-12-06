from scene_entity_systems.components import PygameRenderComponent
from scene_entity_systems.components import PositionComponent, ComponentController
from scene_entity_systems.systems import PositionSystem
import pygame


class PygameRenderSystem:

    position_component_controller: ComponentController

    def __init__(self, arg_position_component_controller: ComponentController) -> None:
        pygame.init()
        self.position_component_controller = arg_position_component_controller
        self.width, self.height = 1280, 720
        self.screen = pygame.display.set_mode((self.width, self.height))

    def render_background(self):
        self.screen.fill((128, 128, 128))
    
    def render_end(self):
        pygame.display.flip()

    def render_circle(self, arg_pygame_render_component: PygameRenderComponent) -> None:
        target_position = self.position_component_controller.get_component(arg_pygame_render_component.entity_id).position
        color = (arg_pygame_render_component.rgb_red, arg_pygame_render_component.rgb_green, arg_pygame_render_component.rgb_blue)
        pygame.draw.circle(self.screen, color, (target_position.x, target_position.y), arg_pygame_render_component.size.x)



