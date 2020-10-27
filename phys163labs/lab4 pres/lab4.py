from vpython import *

scene.height = 720
scene.width = 720

line_x = cylinder(pos=vec(-5, 0, 0), axis=vec(10, 0, 0), radius=0.05)
line_y = cylinder(pos=vec(0, -5, 0), axis=vec(0, 10, 0), radius=0.05)
line_z = cylinder(pos=vec(0, 0, -5), axis=vec(0, 0, 10), radius=0.05)

# TODO: use checkboxs to enable certain attributes, fields, forces etc.

rad = 5  # radius of ring
n = 250  # number of segments
dtheta = 2 * pi / (n)  # spacing between adjacent balls in rod
length = rad * (2 * pi)
seg_length = length / n
ring = []  # creates empty list
POI = vec(2.5, 0, 0)
i = 1  # current
c = 5  # number of current arrows
B_tot = vec(0, 0, 0)


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


B_tot += ring_gen(-5)
B_tot += ring_gen(5)
print(B_tot)
