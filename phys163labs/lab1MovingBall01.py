from vpython import *

ball = sphere(pos=vector(1, 2, 3), color=color.orange, radius=0.5)
velocity = vector(1, 3, 1)
my_arrow = arrow(pos=ball.pos, axis=velocity, color=color.green)
deltat = 0.1
t = 0
while t < 80:
    rate(10)
    ball.pos = ball.pos + velocity * deltat
    t = t + deltat
