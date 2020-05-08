from vpython import *

# task 3
# draw a set of coordinate axes
line_x = cylinder(pos=vec(-10, 0, 0), axis=vec(20, 0, 0), radius=0.05)
line_y = cylinder(pos=vec(0, -10, 0), axis=vec(0, 20, 0), radius=0.05)
line_z = cylinder(pos=vec(0, 0, -10), axis=vec(0, 0, 20), radius=0.05)

G = 6.67e-11  # Universal Gravitation constant
scale_factor = 0.5  # used to scale force arrows (to make arrows visible)
rock1 = sphere(color=color.orange, radius=0.8)
rock2 = sphere(color=color.cyan,
               radius=0.4,
               make_trail=True,
               trail_type="points",
               interval=20,
               retain=500)
rock1.pos = vec(-6, 2, 0)
rock2.pos = vec(5, 0, 0)
rock1.m = 8e10  # defines mass as an attribute of rock1
rock2.m = 2e2  # defines mass as an attribute of rock2
rock2.p = vec(0, 0, 0)  # defines momentum as an attribute of rock2
# r_1to2 goes from 1 towards 2 (center to center)
r_1to2 = rock2.pos - rock1.pos
# compute initial force ON 2
F_1on2 = G * rock1.m * rock2.m * (-r_1to2) / (mag(r_1to2) ** 3)
# draw initial force arrow ON 2
F_1on2_arrow = arrow(pos=rock2.pos, color=rock1.color)
sat_lev = 10

# initialize loop parameters
t = 0
dt = 0.1
sim_speed = 2
while mag(rock1.pos) - mag(rock2.pos) > rock1.radius+rock2.radius:
    rate(sim_speed / dt)
    r_1to2 = rock2.pos - rock1.pos  # update center-to-center vector
    F_1on2 = G * rock1.m * rock2.m * (-r_1to2) / (mag(r_1to2) ** 3)  # update force ON 2
    rock2.p += F_1on2 * dt  # update momentum for rock2
    rock2.pos += rock2.p / rock2.m * dt  # update position for rock2

    if mag(scale_factor * F_1on2) > sat_lev:
        F_1on2_arrow.axis = sat_lev * hat(F_1on2)
    else:
        F_1on2_arrow.axis = scale_factor * F_1on2
    F_1on2_arrow.pos = rock2.pos  # update force arrow position

    t += dt  # increment time
