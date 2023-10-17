import time

class DeltaTime:

    deltaTime: float
    startTime: float

    def __init__(self):
        self.startTime = 0.0
        self.deltaTime = time.time()

    def get(self):
        return self.deltaTime

    def set(self, newDeltaTime: float):
        self.deltaTime = newDeltaTime

    def set_start_frame(self, a_startTime):
        self.startTime = a_startTime

    def calculate(self, a_time: float):
        self.deltaTime = a_time - self.startTime


