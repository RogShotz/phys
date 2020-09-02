from vpython import *

line_x = cylinder(pos=vec(-5, 0, 0), axis=vec(10, 0, 0), radius=0.05)
line_y = cylinder(pos=vec(0, -5, 0), axis=vec(0, 10, 0), radius=0.05)
line_z = cylinder(pos=vec(0, 0, -5), axis=vec(0, 0, 10), radius=0.05)

scale_arrow = .01
k = 8.99e9  # Coulomb constant
L = 5.0  # length of rod
Q = 2.0e-2  # total charge on rod
N = 10  # number of elements in rod

q1 = 2.0e-4
m1 = 100
r1 = vec(0, 0, 2)
p1 = vec(0, 0, 0)
ball1 = sphere(pos=r1, radius=.5, color=vec(1, 0, 0))

R = 5  # radius of ring
dq = Q / N  # charge on a single element
dtheta = 2 * pi / (N)  # spacing between adjacent balls in rod
arc = []  # creates empty list
E_tot = vec(0, 0, 0)  # initialize total electric field vector to zero

T_record = []
f1 = gdots(color=color.red)
f2 = gcurve(color=color.blue)

for theta in arange(0, 2 * pi, dtheta):
    ball = sphere(pos=vec(R * cos(theta), R * sin(theta), 0), radius=0.25)
    ball.dq = dq  # defines charge attribute of ball!!!
    arc.append(ball)  # adds element to list
    r = ball1.pos - ball.pos
    E_tot += k * ball.dq * r / mag(r) ** 3

F_net = -q1 * E_tot
F_arrow = arrow(pos=ball1.pos, axis=scale_arrow * F_net, color=vec(1, 1, 1))

delta_t = 0.01
sim_speed = 1
for t in arange(0, 10, delta_t):
    E_tot = vec(0, 0, 0)
    rate(sim_speed / delta_t)
    p1 += F_net * delta_t  # momentum update equation
    ball1.pos += (p1 / m1) * delta_t  # position update equation
    for i in range(N):  # update charge
        r = ball1.pos - arc[i].pos
        E_tot += k * arc[i].dq * r / mag(r) ** 3
    F_net = -q1 * E_tot
    F_exact = q1 * k * mag(ball1.pos) * Q / (R ** 2 + mag(ball1.pos) ** 2) ** (3 / 2)
    f1.plot(t, mag(F_net))
    f2.plot(t, F_exact)
    print("Percent error: ", (F_exact - mag(F_net)) / mag(F_net) * 100, "%")

    F_arrow.pos = ball1.pos
    F_arrow.axis = scale_arrow * F_net
