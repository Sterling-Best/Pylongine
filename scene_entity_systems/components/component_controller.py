from .component import Component
from .component_factory import ComponentFactory
from .component_repository import ComponentRepository
from .component_manager import ComponentManager
from abc import ABC, abstractmethod
from typing import Callable


class ComponentController(ABC):

    component_factory: ComponentFactory
    component_repository: ComponentRepository
    component_manager: ComponentManager

    @abstractmethod
    def __init__(self):
        pass

    def create_component(self, arg_entity_id: int) -> None:
        target_component = self.component_factory.create_component(arg_entity_id)
        self.component_repository.add_component(arg_entity_id, target_component)

    def remove_component(self, arg_entity_id: int) -> None:
        self.component_repository.remove_component(arg_entity_id)

    def activate_component(self, arg_entity_id: int) -> None:
        self.component_manager.activate_component(self.component_repository.get_component(arg_entity_id))

    def deactivate_component(self, arg_entity_id: int) -> None:
        self.component_manager.deactivate_component(self.component_repository.get_component(arg_entity_id))

    def toggle_active_component(self, arg_entity_id: int) -> None:
        self.component_manager.toggle_active_component(self.component_repository.get_component(arg_entity_id))

    def iterate_components(self, arg_callable: Callable, *args):
        self.component_repository.iterate_repository(arg_callable, *args)

    def iterate_single_component(self, arg_callable: Callable, arg_entity_id: int, *args):
        self.component_repository.iterate_component(arg_callable, arg_entity_id, *args)

    def get_last_key(self) -> int:
        return self.component_repository.get_last_key()

    def get_component(self, entity_id: int) -> Component:
        return self.component_repository.get_component(entity_id)





