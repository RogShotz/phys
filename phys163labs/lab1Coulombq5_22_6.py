from vpython import *

# Lab q 5 WB 22.6
scale_arrow = 1e-8
line_x = cylinder(pos=vec(-10, 0, 0), axis=vec(20, 0, 0), radius=0.05)
line_y = cylinder(pos=vec(0, -10, 0), axis=vec(0, 20, 0), radius=0.05)
line_z = cylinder(pos=vec(0, 0, -10), axis=vec(0, 0, 20), radius=0.05)

# q's are charges in coulombs
q1 = 1
q2 = 1
q3 = 1  # can be pos or neg

# the coulomb constant is k
k = 8.99e9

# r's are initial locations of charges origin at the black dot
r1 = vec(0, 5, 0)
r2 = vec(0, -5, 0)
r3 = vec(5, 0, 0)

# make positive charges red and negative charges blue-green
if q1 > 0:
    c1 = vec(1, 0, 0)
else:
    c1 = vec(0, 0.6, 1)
if q2 > 0:
    c2 = vec(1, 0, 0)
else:
    c2 = vec(0, 0.6, 1)
if q3 > 0:
    c3 = vec(1, 0, 0)
else:
    c3 = vec(0, 0.6, 1)
ball1 = sphere(pos=r1, radius=.5, color=c1)
ball2 = sphere(pos=r2, radius=.5, color=c2)
ball3 = sphere(pos=r3, radius=.5, color=c3)

# determine the coulomb force q2 exerts ON q1 (the small ball)
r_1to3 = ball3.pos - ball1.pos
F_1on3 = k * q1 * q3 * r_1to3 / mag(r_1to3) ** 3
r_2to3 = ball3.pos - ball2.pos
F_2on3 = k * q2 * q3 * r_2to3 / mag(r_2to3) ** 3

# draw an arrow representing the force, scale_arrow changes size of all force arrows
text(text="q1", pos=r1 + vec(0, 1, 0))
text(text="q2", pos=r2 + vec(0, 1, 0))
text(text="Test Charge", pos=r3 + vec(0, 2, 0))

F_arrow_1on3 = arrow(pos=r3, axis=scale_arrow * F_1on3, color=c3)
F_arrow_2on3 = arrow(pos=r3, axis=scale_arrow * F_2on3, color=c3)
F_arrow_neton1 = arrow(pos=r3, axis=scale_arrow * (F_1on3 + F_2on3), color=color.purple)
