from visual import *

# draw a set of coordinate axes
line_x = cylinder(pos=vector(-5, 0, 0), axis=vector(10, 0, 0),
                  radius=0.05)
line_y = cylinder(pos=vector(0, -5, 0), axis=vector(0, 10, 0),
                  radius=0.05)
line_z = cylinder(pos=vector(0, 0, -5), axis=vector(0, 0, 10),
                  radius=0.05)

sigma = 1.0  # AREA mass density of triangle
R = 25.0 # radius
N = 25  # number of slices for triangle, must be >1
center = vector(0, 0, 0)  # specify bottom left corner of triangle
dy = R/N

numer = vector(0, 0, 0)  # initialize numerator of center of mass formula
denom = 0  # initialize denominator of center of mass formula
plate = []  # initialize empty list for organizational purposes
i = 0
y = 0

while y < R:
    chunk = cylinder(radius = 0.25 * dy)
    chunk.area = 2 * sqrt(R**2 - y**2)
    chunk.pos = vector(-chunk.area/4, y*.5, 0)
    chunk.axis = vector(chunk.area/2, 0, 0)
    chunk.dm = sigma * chunk.area * dy
    plate.append(chunk)
    numer += plate[i].dm*(plate[i].pos+0.5*plate[i].axis)
    denom += plate[i].dm
    i += 1
    y += dy

COM = numer / denom

percdiff = ((COM.y - 4/3*R)/(4/3*R))*100
print percdiff
print COM
COM_indicator = sphere(pos=COM, radius= dy,
                       color=vector(1, 0.2, 0.8))
