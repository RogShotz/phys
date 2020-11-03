from vpython import *

scene.height = 720
scene.width = 1080
scale = .0001  # converting calcs down to milimeters (rads are in 10s), also makes it too small for user though

# TODO: use checkboxes to enable certain attributes, fields, forces etc.

# Ring Attributes
ring1pos = -15  # the x position of the ring
ring2pos = -ring1pos
ring3pos = -6
ring4pos = -ring3pos
ring5pos = 0

n = 100  # number of segments
dtheta = 2 * pi / n  # spacing between adjacent balls in rod
ring = []  # creates empty list

# Variable Initializations
i = 1  # current
c = 5  # number of current arrows
B_tot = vec(0, 0, 0)
B = vec(0, 0, 0)
p = vec(0, 0, 0)
z = 0
mu_0 = 4 * pi * 1e-7
k_bio = mu_0 * i / (4 * pi)

# POI Initializations
POI = vec(0, 0, -.2)
ball = sphere(pos=POI, radius=.2, color=color.red, make_trail=True, trail_type="curve")
ball.q = -1.602e-19
ball.v = vec(1.23, -.9, 0)
ball.m = 9.11e-31


def ring_gen(z_pos, rad):  # creates rings
    B_func = vec(0, 0, 0)
    length = rad * (2 * pi)
    seg_length = length / n
    for theta in arange(0, 2 * pi, dtheta):
        segment = cylinder(pos=vec(z_pos, rad * sin(theta), rad * cos(theta)), radius=0.25, color=color.red,
                           axis=vec(0, seg_length * sin(radians(90) - theta), seg_length * cos(theta + radians(90))))
        ring.append(segment)  # cylinder segments of rings

        if (len(ring)) % round((n / c)) == 0:  # construct arrows indicating current
            arrow(pos=vec(z_pos, rad * sin(theta), rad * cos(theta) + segment.radius / 2),
                  axis=vec(0, rad / 1.5 * sin(radians(90) - theta), rad / 1.5 * cos(radians(90) + theta)))

        r = POI - (segment.pos + 0.5 * segment.axis * scale)

        ds = segment.axis * scale
        B_func += k_bio * cross(ds, r) / mag(r) ** 3
    return B_func


def get_b(POI):  # gets b_ext from any POI
    B_new = vec(0, 0, 0)
    for j in range(0, len(ring)):
        r = POI - (ring[j].pos + 0.5 * ring[j].axis * scale)

        ds = ring[j].axis * scale
        B_new += k_bio * cross(ds, r) / mag(r) ** 3
    return B_new


# Ring Generations
out_rad = 2.5
in_rad = 10
B_tot += ring_gen(ring1pos, out_rad)
B_tot += ring_gen(ring2pos, out_rad)
B_tot += ring_gen(ring3pos, in_rad)
B_tot += ring_gen(ring4pos, in_rad)
B_tot += ring_gen(ring5pos, in_rad)

slope_range = abs(ring1pos) + 5  # tweak var at end to expand or shrink slope field range of b arrows
field_max = 1.5e-11
for y in range(-slope_range + 5, slope_range - 5):
    for x in range(-slope_range, slope_range):
        fieldPOI = vec(x, y, z)
        field = get_b(fieldPOI)
        field_arrow = arrow(pos=fieldPOI, axis=hat(field))

        if mag(field) >= 0:
            field_arrow.color = color.green
        else:
            field_arrow.color = color.blue
        if mag(field) > field_max:
            field_arrow.opacity = 1
        if mag(field) < -field_max:
            field_arrow.opacity = 1
        else:
            field_arrow.opacity = mag(field) / field_max

# Animations Initialization
t = 0
dt = .01
simspeed = 10000

while t < 8000 and mag(ball.pos) * 0.8 < ring2pos:
    rate(simspeed / dt)
    B = get_b(ball.pos)
    F = ball.q * cross(ball.v, B)
    print(mag(B))
    ball.v += F * dt / ball.m
    ball.pos += ball.v * dt
    t += dt
