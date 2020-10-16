from vpython import *

scene.height = 720
scene.width = 1280
scene.background = color.black

k = 8.99e9
q1 = -1.0e-9
q2 = 1.0e-9
sat_lev = .3  # max allowable size of an arrow
list_of_arrows = []  # creates empty list for arrows
if q1 > 0:
    c1 = vec(1, 0, 0)
else:
    c1 = vec(0, 0.2, 1)
ball1 = sphere(pos=vec(0, 2, 0), radius=0.3, color=c1)
ball1.q = q1  # define charge as an attribute of the ball
if q2 > 0:
    c2 = vec(1, 0, 0)
else:
    c2 = vec(0, 0.2, 1)
ball2 = sphere(pos=vec(0, 0, 0), radius=0.3, color=c2)
ball2.q = q2  # define charge as an attribute of the ball

for x in range(-5, 6):
    for y in range(-5, 6):
        POI = vec(x, y, 0)
        r1 = vec(POI - ball1.pos)
        r2 = vec(POI - ball2.pos)
        vis = True

        if mag(r1) < ball1.radius or mag(r2) < ball2.radius:
            vis = False  # this field would be infinite...ignore it
        else:
            E_field_1 = k * q1 * r1 / (mag(r1) ** 2)
            E_field_2 = k * q2 * r2 / (mag(r2) ** 2)

        E_field_net = E_field_1 + E_field_2

        opa = mag(E_field_net) * sat_lev
        E_arrow = arrow(pos=POI, axis=hat(E_field_net) * .8, opacity=opa, visible=vis)
        list_of_arrows.append(E_arrow)

for myarrow in list_of_arrows:
    rate(20)
    myarrow.color = c1
