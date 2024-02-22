

class MRFWheel:

    def rotate(self):
        print('MRF Wheel is rotating')


class CEATWheel:
    
    def rotate(self):
        print('CEAT Wheel is rotating')


class Car:

    def __init__(self, wheel):
        self.wheel = wheel

    def set_wheel(self, wheel):
        self.wheel = wheel    

    def move(self):
        self.wheel.rotate()
        print('Car is moving')


mrf_wheel = MRFWheel()
ceat_wheel = CEATWheel()

car1 = Car(mrf_wheel)
car1.move()
car1.move()

car1.set_wheel(ceat_wheel)
car1.move()
car1.move()