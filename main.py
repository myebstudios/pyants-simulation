import turtle
import random

ant_moves = 200 # The number of moves the ants make.

ant1 = turtle.Turtle()
ant1.speed(15)
ant1.color('red')

ant2 = turtle.Turtle()
ant2.speed(15)
ant2.color('blue')

for i in range(ant_moves):

  ant1.forward(random.randint(1, 10))
  ant1.right(random.randint(-45,45))

  ant2.forward(random.randint(1, 10))
  ant2.right(random.randint(-45,45))