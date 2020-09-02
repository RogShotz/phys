from vpython import *

# Arrow and graph
scale_arrow = .1
line_x = cylinder(pos=vec(-10, 0, 0), axis=vec(20, 0, 0), radius=0.05)
line_y = cylinder(pos=vec(0, -10, 0), axis=vec(0, 20, 0), radius=0.05)
line_z = cylinder(pos=vec(0, 0, -10), axis=vec(0, 0, 20), radius=0.05)

# q's are charges in coulombs
q1 = 0.190e-3
q2 = -0.295e-3

# masses
m1 = 1.4
m2 = 1e6

# the coulomb constant is k
k = 8.99e9

# r's are initial locations of charges
r1 = vec(5.8, 0, 0)
r2 = vec(0, 0, 0)

# p=mv
v = sqrt((k*q1*abs(q2))/(m1*r1.x))
print(v)
print(m1*v)

# p's are initial momentums of charges
p1 = vec(0, m1*v, 0)
p2 = vec(0, 0, 0)

# make positive charges red and negative charges blue-green
if q1 > 0:
    c1 = vec(1, 0, 0)
else:
    c1 = vec(0, 0.6, 1)
if q2 > 0:
    c2 = vec(1, 0, 0)
else:
    c2 = vec(0, 0.6, 1)
ball1 = sphere(pos=r1, radius=0.3, color=c1)
ball2 = sphere(pos=r2, radius=1, color=c2)

# determine the coulomb force q2 exerts ON q1 (the small ball)
r_1to2 = ball2.pos - ball1.pos
F_1on2 = k * q1 * q2 * r_1to2 / mag(r_1to2) ** 3

r_2to1 = ball1.pos - ball2.pos
F_2on1 = k * q1 * q2 * r_2to1 / mag(r_2to1) ** 3

print(F_2on1)  # this print statement allows you to check the math

# draw an arrow representing the force, scale_arrow changes size of all force arrows
F_arrow_1on2 = arrow(pos=r2, axis=scale_arrow * F_1on2, color=c2)
F_arrow_2on1 = arrow(pos=r1, axis=scale_arrow * F_2on1, color=c1)

# loop uses NET force ON ball1 to update position and momentum of ball1
# for now assume ball2 remains motionless as m2 >> m1
# WARNING: code produces unphysical results if ball1 moves inside ball2
t = 0
delta_t = 0.001
sim_speed = 1
while t < 30:
    rate(sim_speed / delta_t)
    p1 = p1 + F_2on1 * delta_t  # momentum update equation
    p2 = p2 + F_1on2 * delta_t
    ball1.pos = ball1.pos + (p1 / m1) * delta_t  # position update equation
    ball2.pos = ball2.pos + (p2 / m2) * delta_t

    r_1to2 = ball2.pos - ball1.pos
    F_1on2 = k * q1 * q2 * r_1to2 / mag(r_1to2) ** 3

    r_2to1 = ball1.pos - ball2.pos
    F_2on1 = k * q1 * q2 * r_2to1 / mag(r_2to1) ** 3

    F_arrow_1on2.pos = F_arrow_1on2.pos + (p2 / m2) * delta_t  # update F_2on1 arrow pos
    F_arrow_2on1.pos = F_arrow_2on1.pos + (p1 / m1) * delta_t  # update F_2on1 arrow pos

    F_arrow_1on2.axis = F_1on2 * scale_arrow  # update F_2on1 size
    F_arrow_2on1.axis = F_2on1 * scale_arrow  # update F_2on1 size

    t = t + delta_t  # increment the time
