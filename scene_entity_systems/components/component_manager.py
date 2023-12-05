from .component import Component
from abc import ABC, abstractmethod


class ComponentManager(ABC):

    def __init__(self):
        pass

    def get_entity_id(self, arg_component: Component) -> int:
        return arg_component.component_id

    def activate_component(self, arg_component: Component) -> None:
        arg_component.is_active = True

    def deactivate_component(self, arg_component: Component) -> None:
        arg_component.is_active = False

    def toggle_active_component(self, arg_component: Component) -> None:
        arg_component.is_active = not arg_component.is_active
