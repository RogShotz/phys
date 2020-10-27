from vpython import *
scene.height = 720
scene.width = 720

line_x = cylinder(pos=vec(-5, 0, 0), axis=vec(10, 0, 0), radius=0.05)
line_y = cylinder(pos=vec(0, -5, 0), axis=vec(0, 10, 0), radius=0.05)
line_z = cylinder(pos=vec(0, 0, -5), axis=vec(0, 0, 10), radius=0.05)

scale = 5
# TODO: use checkboxs to enable certain attributes, fields, forces etc.

# Ring Attributes
ring1pos = -10
ring2pos = 10

rad = 2.5  # radius of ring
n = 50  # number of segments
dtheta = 2 * pi / (n)  # spacing between adjacent balls in rod
length = rad * (2 * pi)
seg_length = length / n
ring = []  # creates empty list
ringvis = []
i = 1  # current
c = 5  # number of current arrows
B_tot = vec(0, 0, 0)
B = vec(0, 0, 0)

# POI Initializations
POI = vec(-4, 3, 0)
ball = sphere(pos=POI, radius=.1, color=color.red)
ball.q = 1e-6
ball.v = vec(.5, 1, 0)
ball.m = 1e-6


def ring_gen(z_pos):
    B_func = vec(0, 0, 0)
    for theta in arange(0, 2 * pi, dtheta):
        segment = cylinder(pos=vec(z_pos, rad * sin(theta), rad * cos(theta)), radius=0.25,
                           axis=vec(0, seg_length * sin(radians(90) - theta), seg_length * cos(theta + radians(90))))
        segment.color = color.red
        ring.append(segment)

        if (len(ring)) % round((n / c)) == 0:
            current = arrow(pos=vec(z_pos, rad * sin(theta), rad * cos(theta) + segment.radius / 2),
                            axis=vec(0, rad / 1.5 * sin(radians(90) - theta), rad / 1.5 * cos(radians(90) + theta)))

        r = POI - (segment.pos + 0.5 * segment.axis)

        ds = segment.axis
        B_func += i * cross(ds, r) / mag(r) ** 3

    return B_func


def get_b(POI, z_pos):
    B_new = vec(0, 0, 0)
    for theta in arange(0, 2 * pi, dtheta):
        segment = cylinder(pos=vec(z_pos, rad * sin(theta), rad * cos(theta)), radius=0.25,
                           axis=vec(0, seg_length * sin(radians(90) - theta), seg_length * cos(theta + radians(90))),
                           opacity=0)
        ringvis.append(segment)
        r = POI - (segment.pos + 0.5 * segment.axis)

        ds = segment.axis
        B_new += i * cross(ds, r) / mag(r) ** 3
    return B_new


# Ring Generations
B_tot += ring_gen(ring1pos)
B_tot += ring_gen(ring2pos)

# Animations Initialization
t = 0
dt = .001
simspeed = 5

F_arrow = arrow(pos=ball.pos,axis=vec(0, 0, 0), color=color.green)
v_arrow = arrow(pos=ball.pos, axis=ball.v, color=color.red)
while t < 40:
    rate(simspeed / dt)
    B += get_b(ball.pos, ring1pos)
    F = ball.q * cross(ball.v, B)
    ball.v += F * dt / ball.m
    ball.pos += ball.v * dt

    F_arrow.pos = ball.pos
    F_arrow.axis = scale * F

    v_arrow.pos = ball.pos
    v_arrow.axis = ball.v

    t += dt
print(B_tot)