from visual import *

#draw a set of coordinate axes
line_x=cylinder(pos=vector(-5, 0, 0), axis=vector(10, 0, 0), radius=0.05)
line_y=cylinder(pos=vector(0, -5, 0), axis=vector(0, 10, 0), radius=0.05)
line_z=cylinder(pos=vector(0, 0, -5), axis=vector(0, 0, 10), radius=0.05)
lamb = 1.0 #LINEAR mass density of rod
L = 5.1 #length of rod
N = 21 #number of slices for rod, must be >1
left_end = vector(0, 0, 0) #specify location of left end of rod
dx = L/N #compute size of slice

numer = vector(0,0,0) #initialize numerator of center of mass formula
denom = 0 #initialize denominator of center of mass formula
rod = [] #initialize list for organizational purposes
i = 0 #initialize increment parameter
while (i < N):
    ball = sphere(pos=left_end+vector(i*dx,0,0), radius=dx)
    ball.dm = lamb*dx #define & compute mass of slice
    rod.append(ball)
    numer += rod[i].dm*rod[i].pos
    denom += rod[i].dm
    i += 1
COM = numer/denom
print"Center of mass is at", COM
COM_indicator = pyramid(pos=COM,
size=3*vector(dx,dx,dx),
color=vector(1, 0.2, 0.8)) 
