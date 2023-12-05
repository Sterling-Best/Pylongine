from abc import ABC, abstractmethod, abstractproperty
from .component import Component


class ComponentFactory(ABC):

    component_count: int

    def __init__(self):
        self.component_count = 0

    def create_component(self, arg_entity_id: int) -> Component:
        target_component = self._setup_component(self.component_count, arg_entity_id)
        self.component_count += 1
        target_component.is_active = True
        return target_component

    @abstractmethod
    def _setup_component(self, arg_component_count: int, arg_entity_id: int) -> Component:
        pass
