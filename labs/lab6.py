from vpython import *

# task 1
# draw a set of coordinate axes
line_x = cylinder(pos=vec(-10, 0, 0), axis=vec(20, 0, 0), radius=0.05)
line_y = cylinder(pos=vec(0, -10, 0), axis=vec(0, 20, 0), radius=0.05)
line_z = cylinder(pos=vec(0, 0, -10), axis=vec(0, 0, 20), radius=0.05)

G = 6.67e-11  # Universal Gravitation constant
scale_factor = 0.5  # used to scale force arrows (to make arrows visible)
rock1 = sphere(color=color.orange, radius=0.8)
rock2 = sphere(color=color.cyan, radius=0.4)
rock1.pos = vec(-6, 2, 0)
rock2.pos = vec(5, 0, 0)
rock1.m = 8e6  # defines mass as an attribute of rock1
rock2.m = 2e6  # defines mass as an attribute of rock2
# r_1to2 goes from 1 towards 2 (center to center)
r_1to2 = rock2.pos - rock1.pos
# Compute the force
# F_1on2 points in the negative r_1to2 hat
# in pracitce it is easier to code r-vector/r^3 than r-hat/r^2
F_1on2 = G * rock1.m * rock2.m * (-r_1to2) / (mag(r_1to2) ** 3)
# when drawing forces ON 2, the tails of the force arrows should be ON 2
F_1on2_arrow = arrow(pos=rock2.pos, color=rock1.color)
sat_lev = 10
if mag(scale_factor * F_1on2) > sat_lev:
    F_1on2_arrow.axis = sat_lev * hat(F_1on2)
else:
    F_1on2_arrow.axis = scale_factor * F_1on2

# Compute the potential energy
U_12 = -G * rock1.m * rock2.m / mag(r_1to2)
print('The gravitational FORCE is ' + F_1on2 + ' N.')
print('The MAGNITUDE of gravitational force ON 2 is ' + mag(F_1on2) + ' N.')
print('The gravitational potential energy is ' + U_12 + ' J.')
