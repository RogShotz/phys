from vpython import *

# WB 21.3
# Arrow and graph
scale_arrow = .5e-3
scale_ball = 1e-3

# q's are charges in coulombs
q1 = -3e-6  # q3 in question
q2 = -2e-6
q3 = 1e-6  # q1 in question

# masses
m1 = 1
m2 = 2000
m3 = 2000

# the coulomb constant is k
k = 8.99e9

# r's are initial locations of charges
r1 = vec(0, 0, 0)
r2 = vec(0.03, 0.04, 0)
r3 = vec(0, 0.04, 0)

# p's are initial momentums of charges
p1 = vec(3.3, -3.3, 0)
p2 = vec(0, 0, 0)
p3 = vec(0, 0, 0)

# make positive charges red and negative charges blue-green
if q1 > 0:
    c1 = vec(1, 0, 0)
else:
    c1 = vec(0, 0.6, 1)
if q2 > 0:
    c2 = vec(1, 0, 0)
else:
    c2 = vec(0, 0.6, 1)
if q2 > 0:
    c3 = vec(1, 0, 0)
else:
    c3 = vec(0, 0.6, 1)
ball1 = sphere(pos=r1, radius=1 * scale_ball, color=c1)
ball2 = sphere(pos=r2, radius=1 * scale_ball, color=c2)
ball3 = sphere(pos=r3, radius=1 * scale_ball, color=c1)

# determine the coulomb force q2 exerts ON q1 (the small ball)
r_2to1 = ball1.pos - ball2.pos  # final position minus initial position
F_2on1 = k * q1 * q2 * r_2to1 / mag(r_2to1) ** 3
r_3to1 = ball1.pos - ball3.pos
F_3on1 = k * q1 * q3 * r_3to1 / mag(r_3to1) ** 3
print(F_2on1)  # this print statement allows you to check the math
print(F_3on1)

# draw an arrow representing the force, scale_arrow changes size of all force arrows
F_arrow_2on1 = arrow(pos=r1, axis=scale_arrow * F_2on1, color=c1)
F_arrow_3on1 = arrow(pos=r1, axis=scale_arrow * F_3on1, color=c2)
F_arrow_neton1 = arrow(pos=r1, axis=scale_arrow * (F_2on1 + F_3on1), color=color.purple)
