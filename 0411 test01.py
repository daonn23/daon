class Car:
    def __init__(self,name,year):
        self.name = name
        self.year = year
        self.speed = 0
        
    def upSpeed(self, value):
        self.speed += value

    def reset(self):
        self.speed = 0

class Sedan(Car):
    def upSpeed(self, value):
        self.speed += value

        if self.speed >150:
            self.speed = 150

    def downSpeed(self, value):
        self.speed -= value

        if self.speed < 0:
            self.speed = 0


myCar = Sedan('Volvo', 2023)

myCar.upSpeed(50)
myCar.upSpeed(30)
myCar.reset()

print(myCar.speed)
