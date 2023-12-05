from .component import Component
from typing import Callable
from abc import ABC, abstractmethod


class ComponentRepository(ABC):

    component_repository: dict[int, Component]

    def __init__(self):
        self.component_repository = {}

    def add_component(self, arg_entity_id: int, arg_component: Component) -> None:
        self.component_repository[arg_entity_id] = arg_component

    def remove_component(self, arg_entity_id: int) -> None:
        del self.component_repository[arg_entity_id]

    def get_component(self, arg_entity_id: int) -> Component:
        return self.component_repository[arg_entity_id]

    def iterate_component(self, arg_callable: Callable, arg_entity_id: int, *args):
        arg_callable(self.component_repository[arg_entity_id], *args)

    def iterate_repository(self, arg_callable: Callable, *args) -> None:
        for entity_id in self.component_repository:
            arg_callable(self.component_repository[entity_id], *args)

    def clear_repository(self) -> None:
        self.component_repository.clear()

    def get_last_key(self) -> int:
        return next(reversed(self.component_repository))

    def get_last_component(self) -> Component:
        return self.get_component(self.get_last_key())
