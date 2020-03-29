from visual import *
#this code sketches out how you might do vector addition
#to do 2D vector addition, keep z-components of any vectors equal to zero
#draw a set of coordinate axes
line_x=cylinder(pos=vector(-10, 0, 0), axis=vector(20, 0, 0), radius=0.05)
line_y=cylinder(pos=vector(0, -10, 0), axis=vector(0, 20, 0), radius=0.05)
line_z=cylinder(pos=vector(0, 0, -10), axis=vector(0, 0, 20), radius=0.05)
#create a vectortor named A
A = vector(6,8,9)
B = vector(-4,4,-3)
C = vector(1,-5,3)
#draw an arrow corresponding to vector A
A_arrow = arrow(pos=vector(0,0,0),
    axis=A,
    shaftwidth=0.4,
    color=color.red)
A_ball = sphere(pos=vector(0,0,0),
    radius=0.4,
    color=color.green)
B_arrow = arrow(pos=A,
    axis=B,
    shaftwidth=0.4,
    color=color.blue)
B_ball = sphere(pos=A,
    radius=0.4,
    color=color.green)
C_arrow = arrow(pos=A+B,
    axis=C,
    shaftwidth=0.4,
    color=color.yellow)
C_ball = sphere(pos=A+B,
    radius=0.4,
    color=color.green)
R_arrow = arrow(pos=(0,0,0),
    axis=A+B+C,
    shaftwidth=0.4,
    color=color.green)
R_ball = sphere(pos=A+B+C,
    radius=0.4,
    color=color.green)
