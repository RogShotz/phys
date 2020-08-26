from vpython import *

# Arrow and graph
scale_arrow = 1
line_x=cylinder(pos=vec(-10, 0, 0), axis=vec(20, 0, 0), radius=0.05)
line_y=cylinder(pos=vec(0, -10, 0), axis=vec(0, 20, 0), radius=0.05)
line_z=cylinder(pos=vec(0, 0, -10), axis=vec(0, 0, 20), radius=0.05)

# q's are charges in coulombs
q1 = 1.0e-4  # 0.1 mC
q2 = -2.0e-4  # 0.2 mC
q3 = 2.0e-4

# masses
m1 = 1
m2 = 2000
m3 = 2000

# the coulomb constant is k
k = 8.99e9

# r's are initial locations of charges
r1 = vec(5, 5, 0)
r2 = vec(0, 0, 0)
r3 = vec(10, 0, 0)

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
ball1 = sphere(pos=r1, radius=0.3, color=c1)
ball2 = sphere(pos=r2, radius=1, color=c2)
ball3 = sphere(pos=r3, radius=1, color=c1)

# determine the coulomb force q2 exerts ON q1 (the small ball)
r_2to1 = ball1.pos - ball2.pos  # final position minus initial position
F_2on1 = k * q1 * q2 * r_2to1 / mag(r_2to1) ** 3
r_3to1 = ball1.pos - ball3.pos
F_3on1 = k * q1 * q3 * r_3to1 / mag(r_3to1) ** 3
print(F_2on1)  # this print statement allows you to check the math
print(F_3on1)
print(F_3on1+F_2on1)

# draw an arrow representing the force, scale_arrow changes size of all force arrows
F_arrow_2on1 = arrow(pos=r1, axis=scale_arrow * F_2on1, color=c1)
F_arrow_3on1 = arrow(pos=r1, axis=scale_arrow * F_3on1, color=c2)
F_arrow_neton1 = arrow(pos=r1, axis=scale_arrow * (F_2on1 + F_3on1), color=color.purple)
