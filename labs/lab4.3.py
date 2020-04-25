from visual import *

# draw a set of coordinate axes
line_x = cylinder(pos=vector(-5, 0, 0), axis=vector(10, 0, 0),
                  radius=0.05)
line_y = cylinder(pos=vector(0, -5, 0), axis=vector(0, 10, 0),
                  radius=0.05)
line_z = cylinder(pos=vector(0, 0, -5), axis=vector(0, 0, 10),
                  radius=0.05)
sigma = 1.0  # AREA mass density of triangle
L = 6.0  # length of triangle
H = 3.0  # height of triangle
N = 41  # number of slices for triangle, must be >1
left_end = vector(0, 0, 0)  # specify bottom left corner of triangle

# the following parameters relate to the triangle we are creating
# the word "slice" has a special meaning in python
# in my code I chose to use the word "chunk" instead of "slice"

dx = L / N
slope = -H / L
intercept = left_end + vector(0, H, 0)

numer = vector(0, 0, 0)  # initialize numerator of center of mass formula
denom = 0  # initialize denominator of center of mass formula
plate = []  # initialize empty list for organizational purposes
i = 0  # initialize increment parameter
while i < N:
    chunk = cylinder(pos=left_end + vector(i * dx, 0, 0), radius=0.45
                     * dx)
    chunk.axis = vector(0, slope * chunk.pos.x + intercept.y, 0)  # get chunk height
    chunk.dm = sigma * chunk.axis.y * dx  # get chunk mass
    plate.append(chunk)
    numer += plate[i].dm * (plate[i].pos + 0.5 * plate[i].axis)
    denom += plate[i].dm
    i += 1
COM = numer / denom
print COM
COM_indicator = pyramid(pos=COM, size=3 * vector(dx, dx, dx),
                        color=vector(1, 0.2, 0.8))
