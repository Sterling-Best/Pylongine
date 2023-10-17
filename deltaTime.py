import time

class DeltaTime:

    delta_time: float
    start_time: float

    def __init__(self):
        self.start_time = 0.0
        self.delta_time = time.time()

    def get(self):
        return self.delta_time

    def set(self, a_new_delta_time: float):
        self.delta_time = a_new_delta_time

    def set_start_frame(self, a_start_time: float):
        self.start_time = a_start_time

    def calculate(self, a_time: float):
        self.delta_time = a_time - self.start_time


