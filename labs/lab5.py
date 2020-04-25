from vpython import *

scene = canvas(title='Rotational Kinematics',
               width=800, height=600, center=vec(0, 0, 0),  # camera LOOKS AT this point
               background=vec(1, 1, 1))  # makes background white
scene.range = 1.1  # predefines a nice zoom-in level
# define a ball's acceleration as well as initial position & initial velocity
theta_degrees = 15  # this is the angle in DEGREES
theta = radians(theta_degrees)  # this converts that angle to RADIANS
thetaTot = theta
omega = 3.33  # units are RADIANS/sec
alpha = -0.555  # units are RADIANS/sec**2
rotation_axis = vec(0, 0, 1)  # specifies axis of rotation as the z-axis
scale = .3
# create a simulation speed scalar
# a value of 1 will play the sim at real time, less than 1 gives slo mo
sim_speed = 1
# initialize the clock time and time increment size
# tip: period = 2*pi/omega...dt<(min period)/100 should be fairly accurate
# tip: max eye refresh rate is 30 frames per sec..dt<0.03 is smooth to eye
t = 0
dt = 0.03
# draw a pivot at the center of the screen
pivot = sphere(pos=vec(0, 0, 0), radius=0.01, color=color.magenta)
# draw a horionztal rod of length 1
rod = cylinder(pos=pivot.pos, radius=0.01, axis=vec(1, 0, 0), color=color.red)
# draw a ball on the rod (imagine this is like a bug that landed on the rod)
bug_r = 0.7  # this is the radius from pivot to bug
bug = sphere(pos=rod.pos + vec(bug_r, 0, 0),
             radius=0.02,
             color=color.blue,
             make_trail=True,
             trail_type="points",
             interval=2,
             retain=20,
             trail_radius=0.005)
# rotate rod and bug to correct initial angle (must use RADIANS when rotating)
rod.rotate(angle=theta, axis=rotation_axis, origin=pivot.pos)
bug.rotate(angle=theta, axis=rotation_axis, origin=pivot.pos)
velArrow = arrow(pos=bug.pos, axis=vec(0, 0, 0))
velArrow.rotate(angle=theta, axis=rotation_axis)
aCenArrow = arrow(pos=bug.pos, ais=vec(0, 0, 0))
# draw & label a set of coordinate axes
# create this code using cut & paste from a previous
# finally we are ready to code the rotation of the rod
dtheta = 0  # initialize CHANGE in angle (in RADIANS)
while t < 7:
    rate(sim_speed / dt)  # determine frames per sec in sim
    omega += alpha * dt  # updates omega
    dtheta = omega * dt  # determines CHANGE in angle
    thetaTot += dtheta

    rod.rotate(angle=dtheta,  # rotate rod by CHANGE in angle
               axis=rotation_axis,  # said another way, updates angular
               origin=pivot.pos)  # position of rod
    bug.rotate(angle=dtheta,  # rotate bug by CHANGE in angle
               axis=rotation_axis,  # said another way, updates angular
               origin=pivot.pos)  # position of bug

    omegaVec = omega * rotation_axis
    alphaVec = alpha * rotation_axis

    rotVel = cross(omegaVec, bug.pos)
    velArrow.pos = bug.pos
    velArrow.axis = rotVel * scale

    aTan = cross(alphaVec, bug.pos)

    aCen = cross(omegaVec, rotVel)
    aCenArrow.pos = bug.pos
    aCenArrow.axis = aCen * scale

    alphaTot = aTan + aCen

    t += dt

    # Omega is in radians per second convert to rotations per minute
    # Final Angular Displacement is final-initial pos

    print("angular velocity: ", omega, " RPMS: ", omega * 60 / (2 * pi), " Final Angular Pos: ", thetaTot)
    print("Final Angular Displacement: ", degrees(thetaTot - theta), " Alpha/ Tangential: ", mag(aTan))
    print("Alpha Centripetal Vec: ", mag(aCen), " Alpha Total: ", mag(alphaTot))

print("Alpha Total Angle = ", degrees(atan(alphaTot.y / alphaTot.x)))
print("Alpha Total Angle Rel + X = ", degrees(atan(alphaTot.y / alphaTot.x)) + 180)

alphaTotArrow = arrow(pos=bug.pos, axis=alphaTot * .5, color=color.blue)