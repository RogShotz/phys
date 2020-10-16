from vpython import *

# draw a set of coordinate axes
line_x = cylinder(pos=vec(-5, 0, 0), axis=vec(10, 0, 0), radius=0.05)
line_y = cylinder(pos=vec(0, -5, 0), axis=vec(0, 10, 0), radius=0.05)
line_z = cylinder(pos=vec(0, 0, -5), axis=vec(0, 0, 10), radius=0.05)

scale_arrow = 1e-2
k = 8.99e9  # Coulomb constant
L = 5.0  # length of rod
Q = -40.2e-9  # total charge on rod
N = 36  # number of elements in rod
dtheta = (2 * pi - radians(27.6)) / (N - 1)
dq = Q / N  # charge on a single element
spacing = L / (N - 1)  # spacing between adjacent balls in rod
c_plus = vec(1, 0, 0)  # will be used as color vector for + charges = red
c_neg = vec(0, 0.5, 1)  # will be used as color vector for - charges = blue-cyan
arc = []  # creates empty list
E_tot = vec(0, 0, 0)  # initialize total electric field vector to zero
R = .467

for theta in arange(0, 2 * pi - radians(27.6), dtheta):
    ball = sphere(pos=vec(R * cos(theta), R * sin(theta), 0), radius=0.25)
    ball.dq = dq  # defines charge attribute of ball!!!
    arc.append(ball)  # adds element to list

r = 0

E_approx = vec(0, 0, 0)
POI = vec(0, 0, 0)  # name a point of interest
for ball in arc:
    r = POI - ball.pos
    E_approx += (k * ball.dq * r) / (mag(r) ** 3)
E_exact = k * Q * POI / (R ** 2 + POI.z ** 2) ** 1.5
print(E_approx)
print(E_exact)