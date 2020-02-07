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
  ant1_walk = random.randint(1, 10)
  ant2_walk = random.randint(1, 10)

  ant1_turn = random.randint(-45,45)
  ant2_turn = random.randint(-45,45)

  ant1.forward(ant1_walk)
  ant1.right(ant1_turn)

  ant2.forward(ant2_walk)
  ant2.right(ant2_turn)