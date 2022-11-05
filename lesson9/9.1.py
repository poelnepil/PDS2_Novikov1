class Car(object):
    def __init__(self, mark, color, engine_capacity):
        self.mark = mark
        self.color = color
        self.engine_capacity = engine_capacity

    def moving_forward(self):
        return 'the car is moving forward'

    def moving_backwards(self):
        return 'the car is moving backwards'


class NewCar(Car):
    def turn_right(self):
        return 'the car turns right'
    def turn_left(self):
        return 'the car turns left'

obj1 = NewCar('bmw', 'black', 2.9)
print(obj1.mark)
print(obj1.moving_forward())
print(obj1.turn_left())