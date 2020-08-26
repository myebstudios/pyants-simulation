import turtle
import random


class Ant(turtle.Turtle):
    def __init__(self, shape='arrow', speed=1, color='black'):
        turtle.Turtle.__init__(self)
        self.speed(speed)
        self.color(color)
        self.shape(shape)

    def run(self, moves):
        for i in range(moves):
            self.forward(random.randint(1, 10))
            self.right(random.randint(-45, 45))


Ant(shape="turtle", color="green", speed=10).run(200)
Ant(color="brown", speed=5).run(100)

turtle.done()
