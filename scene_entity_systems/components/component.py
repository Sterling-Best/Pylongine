class Component:

    component_id: int
    entity_id: int
    is_active: bool

    def __init__(self, arg_component_id: int, arg_entity_id: int):
        self.component_id = arg_component_id
        self.entity_id = arg_entity_id
        self.is_active = True



