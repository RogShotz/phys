from visual import *

# Axes
line_x = cylinder(pos=vector(-10, 0, 0), axis=vector(20, 0, 0),
                  radius=0.05)
line_y = cylinder(pos=vector(0, -10, 0), axis=vector(0, 20, 0),
                  radius=0.05)
line_z = cylinder(pos=vector(0, 0, -10), axis=vector(0, 0, 20),
                  radius=0.05)

# input vectors
A = vector(3, 4, 2) # First Cross / Angle Var
B = vector(-4, 2, -3) # Second Cross / Angle Var
C = vector(1, -5, 3)
R = A + B + C
# Cross Multiplied Vectors
ABCross = vector(A.y * B.z - A.z * B.y, A.z * B.x - A.x * B.z, A.x
                 * B.y - A.y * B.x)  # Foil A X B
# Angle Between Vectors
AMag = sqrt(A.x ** 2 + A.y ** 2 + A.z ** 2)  # ** is exponents
BMag = sqrt(B.x ** 2 + B.y ** 2 + B.z ** 2)
ABRad = acos((A.x * B.x + A.y * B.y + A.z * B.z) /
             (AMag * BMag))  # Calculates in rads
ABAngle = ABRad * (180 / pi)  # AB Angle converted to degrees

# Arrows / Ball points
A_arrow = arrow(pos=vector(0, 0, 0), axis=A, shaftwidth=0.4,
                color=color.red)
A_ball = sphere(pos=vector(0, 0, 0), radius=0.4,
                color=color.green)
B_arrow = arrow(pos=A, axis=B, shaftwidth=0.4,
                color=color.blue)
B_ball = sphere(pos=A, radius=0.4,
                color=color.green)
C_arrow = arrow(pos=A + B, axis=C, shaftwidth=0.4,
                color=color.yellow)
C_ball = sphere(pos=A + B, radius=0.4,
                color=color.green)
R_arrow = arrow(pos=vector(0, 0, 0), axis=R, shaftwidth=0.4,
                color=color.green)
R_ball = sphere(pos=A + B + C, radius=0.4,
                color=color.green)
BCross_arrow = arrow(pos=vector(0, 0, 0), axis=B, shaftwidth=0.4,
                color=color.blue) #since A is already drawn at origin
RCross_arrow = arrow(pos=vector(0, 0, 0), axis=ABCross, shaftwidth=0.4,
                color=color.green)
print ("R =", R, "; A X B =", ABCross, "; Angle Between A and B =", ABAngle)
