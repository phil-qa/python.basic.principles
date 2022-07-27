class Car():
    def __init__(self, registration):
        self.speed=0
        self.reg=registration
        self._accelleration_rate = 100

    def accelerate(self, accelerate_by):
        self._increase_speed(accelerate_by)

    def _increase_speed(self, value):
        self.speed += self._accelleration_rate * value



car = Car("VIP 100")
print(car.reg)
print(car.speed)
car.accelerate(10)
print(car.speed)