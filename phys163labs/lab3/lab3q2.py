from vpython import *

scene.height = 720
scene.width = 1280
scene.background = color.white

# place a charge & define charge attribute .q
ball1 = sphere(pos=vec(-1.5, 1.5, 0), radius=0.25, color=color.red)
ball1.q = 1.0e-9

ball2 = sphere(pos=vec(1.5, 1.5, 0), radius=0.25, color=color.blue)
ball2.q = -1.0e-9
# coulomb constant & define the size of gird spacing & initialize parameters

k_e = 8.99e9
dx = 0.5
V_max = 15

my_plot = gcurve()

for x in arange(-4, 4.01, 0.15):
    for y in arange(-4, 4.01, 0.15):
        POI = vec(x, y, 0)
        plate = box(pos=POI, size=vec(0.15, 0.15, 0.15))
        r1 = (POI - ball1.pos)
        r2 = (POI - ball2.pos)

        if r1 == 0 or r2 == 0:
            V = V_max
        else:
            V = k_e * ball1.q / mag(r1) + k_e * ball2.q / mag(r2)
        if V >= 0:
            plate.color = color.red
        else:
            plate.color = color.blue
        if V > V_max:
            plate.opacity = 1
        if V < -V_max:
            plate.opacity = 1
        else:
            plate.opacity = abs(V) / V_max

        if -0.01 <= y <= 0.14:
            my_plot.plot(x, V)
