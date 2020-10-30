from vpython import *

scene.height = 720
scene.width = 720
scale = 5

# TODO: use checkboxes to enable certain attributes, fields, forces etc.

# Ring Attributes
ring1pos = -10  # the x position of the ring
ring2pos = -ring1pos
rad = 2.5  # radius of ring
n = 100  # number of segments
dtheta = 2 * pi / n  # spacing between adjacent balls in rod
length = rad * (2 * pi)
seg_length = length / n
ring = []  # creates empty list

# Variable Initializations
i = 50  # current
c = 5  # number of current arrows
B_tot = vec(0, 0, 0)
B = vec(0, 0, 0)
p = vec(0, 0, 0)
z = 0
dx = 1
dy = 1

# POI Initializations
POI = vec(0, 0, -.2)
ball = sphere(pos=POI, radius=.2, color=color.red, make_trail=True, trail_type="curve")
ball.q = e - 6
ball.v = vec(.1, -.05, 0)
ball.m = e - 100


def ring_gen(z_pos):
    B_func = vec(0, 0, 0)
    for theta in arange(0, 2 * pi, dtheta):  # create rings
        segment = cylinder(pos=vec(z_pos, rad * sin(theta), rad * cos(theta)), radius=0.25, color=color.red,
                           axis=vec(0, seg_length * sin(radians(90) - theta), seg_length * cos(theta + radians(90))))
        ring.append(segment)  # cylinder segments of rings

        if (len(ring)) % round((n / c)) == 0:  # construct arrows indicating current
            arrow(pos=vec(z_pos, rad * sin(theta), rad * cos(theta) + segment.radius / 2),
                  axis=vec(0, rad / 1.5 * sin(radians(90) - theta), rad / 1.5 * cos(radians(90) + theta)))

        r = POI - (segment.pos + 0.5 * segment.axis)

        ds = segment.axis
        B_func += i * cross(ds, r) / mag(r) ** 3
    return B_func


def get_b(POI):
    B_new = vec(0, 0, 0)
    for j in range(0, len(ring)):
        r = POI - (ring[j].pos + 0.5 * ring[j].axis)

        ds = ring[j].axis
        B_new += i * cross(ds, r) / mag(r) ** 3
    return B_new


# Ring Generations
B_tot += ring_gen(ring1pos)
B_tot += ring_gen(ring2pos)

slope_range = abs(ring1pos) + 5  # tweak var at end to expand or shrink range of b arrows

for y in range(-slope_range, slope_range):
    for x in range(-slope_range, slope_range):
        fieldPOI = vec(x, y, z)
        field = get_b(fieldPOI)
        field_arrow = arrow(pos=fieldPOI, axis=hat(field), color=color.green)

# Animations Initialization
t = 0
dt = .1
simspeed = 1000

while t < 8000:
    rate(simspeed / dt)
    B = get_b(ball.pos)
    F = ball.q * cross(ball.v, B)
    print(mag(B))
    ball.v += F * dt / ball.m
    ball.pos += ball.v * dt
    if mag(ball.pos) * 0.8 > ring2pos:  # stops the loops so it doesnt zoom out because of a launched particle
        break
    t += dt
