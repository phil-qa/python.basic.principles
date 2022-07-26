class Car():
    def __init__(self, registration):
        self.speed=0
        self.reg=registration

    def accelerate(self):
        self.speed += 5



car = Car("VIP 100")
print(car.reg)
print(car.speed)
car.accelerate()
print(car.speed)