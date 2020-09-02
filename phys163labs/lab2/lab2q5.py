from vpython import *

# draw a set of coordinate axes
line_x = cylinder(pos=vec(-5, 0, 0), axis=vec(10, 0, 0), radius=0.05)
line_y = cylinder(pos=vec(0, -5, 0), axis=vec(0, 10, 0), radius=0.05)
line_z = cylinder(pos=vec(0, 0, -5), axis=vec(0, 0, 10), radius=0.05)

scale_arrow = 1e-2
alpha = 10
k = 8.99e9  # Coulomb constant
L = 5.0  # length of rod
Q = 5.0e-7  # total charge on rod
N = 8  # number of elements in rod
a = 2.0  # distance from origin to rod's left end
POI = vec(0, 0, 0)  # name a point of interest
dq = Q / N  # charge on a single element
dq_max = a + L
dx = L / (N - 1)  # spacing between adjacent balls in rod
c_plus = vec(1, 0, 0)  # will be used as color vector for + charges = red
c_neg = vec(0, 0.5, 1)  # will be used as color vector for - charges = blue-cyan
rod = []  # creates empty list
E_tot = vec(0, 0, 0)  # initialize total electric field vector to zero

for i in range(N):
    ball = sphere(pos=vec(a + i * dx, 0, 0), radius=0.25)
    ball.dq = alpha * (ball.pos.x ** 2) * dx
    if ball.dq >= 0:
        ball.color = vec(0.2 + 0.8 * ball.dq / dq_max, 0, 0)  # more charge brighter color
    else:
        ball.color = vec(0, 0.12 + 0.48 * ball.dq / dq_max, 0.2 + 0.8 * ball.dq / dq_max)
    ball.charge = dq  # defines charge attribute of ball!!!
    if ball.charge >= 0:
        ball.color = c_plus  # makes positive charges color vec c_plus
    else:  # makes negative charges color vec c_neg
        ball.color = c_neg
    rod.append(ball)  # adds element to list
    r = POI - rod[i].pos
    E_tot = E_tot + k * rod[i].charge * r / mag(r) ** 3

E_final = arrow(pos=POI, axis=scale_arrow * E_tot, color=rod[0].color)
print(mag(E_tot))

E_exact_mag = k * Q / (a * (L + a))
print(E_exact_mag)

print((E_exact_mag - mag(E_tot)) / mag(E_tot) * 100)
