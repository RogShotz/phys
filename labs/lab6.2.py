from vpython import *

# task 4
# draw a set of coordinate axes
line_x = cylinder(pos=vec(-10, 0, 0), axis=vec(20, 0, 0), radius=0.05)
line_y = cylinder(pos=vec(0, -10, 0), axis=vec(0, 20, 0), radius=0.05)
line_z = cylinder(pos=vec(0, 0, -10), axis=vec(0, 0, 20), radius=0.05)
curve = gcurve(color=color.red)

G = 6.67e-11  # Universal Gravitation constant
scale_factor = 0.5  # used to scale force arrows (to make arrows visible)
rock1 = sphere(color=color.orange, radius=0.8)
rock2 = sphere(color=color.cyan,
               radius=0.4,
               make_trail=True,
               trail_type="points",
               interval=1000,
               retain=500)
rock1.pos = vec(0, 0, 0)
rock2.pos = vec(5, 0, 0)
rock1.m = 8E10  # defines mass as an attribute of rock1 8 * 10 ** 6
rock2.m = 2E2  # defines mass as an attribute of rock2 2 * 10 ** 6
r = mag(rock2.pos - rock1.pos)
perigee = mag(rock2.pos - rock1.pos)
v = sqrt(G * rock1.m / r)
circularOrbitP = rock2.m * v
period = 2 * pi * r / v
rock2.p = vec(0, 120, 0)  # defines momentum as an attribute of rock2
rock1.p = vec(0, 0, 0)
# r_1to2 goes from 1 towards 2 (center to center)
r_1to2 = rock2.pos - rock1.pos
# compute initial force ON 2
F_1on2 = G * rock1.m * rock2.m * (-r_1to2) / (mag(r_1to2) ** 3)
# draw initial force arrow ON 2
sat_lev = 10

# initialize loop parameters
t = 0
dt = .01  # .36 is the approximate value for instability
sim_speed = 200
print("velocity: " + str(v))
print("period: " + str(period))
while t < 1600:
    rate(sim_speed / dt)
    r_1to2 = rock2.pos - rock1.pos  # update center-to-center vector
    F_1on2 = G * rock1.m * rock2.m * (-r_1to2) / (mag(r_1to2) ** 3)  # update force ON 2
    rock2.p += F_1on2 * dt  # update momentum for rock2
    rock1.p += -F_1on2 * dt
    rock2.pos += rock2.p / rock2.m * dt  # update position for rock2
    rock1.pos += rock1.p / rock1.m * dt
    if perigee > mag(rock2.pos - rock1.pos):
        perigee = mag(rock2.pos - rock1.pos)

    t += dt  # increment time
    curve.plot(t, mag(r_1to2))

print(perigee)
