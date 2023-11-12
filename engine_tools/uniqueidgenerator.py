class UniqueIDGenerator:

    id_type_indicator: str
    id_counter: int

    def __init__(self, arg_id_type_indicator):
        self.id_type_indicator = arg_id_type_indicator
        self.id_counter = 0

    def generate_id(self) -> str:
        target_id = str(self.id_type_indicator) + "-" + str(self.id_counter)
        self.id_counter = self.id_counter + 1
        return target_id
