from visual import *

#angle of block1 in DEGREES
angle_degrees = 30

#convert angle to RADIANS
theta = radians(angle_degrees)

#static and kinetic coefficients
#note: code will only produce reasonable results when mu_k < mu_s
mu_s = 0.5
mu_k = 0.3

#initialize mass1 and magnitude of freefall acceleration
g = 9.8
mass1 = 1.0 # hockey puck
mass2 = .2 # prediction

#useful for drawing arrows with mags
scale_arrow = 0.5

#draw a horizontal board
incline = box(pos = vector(0, 0, 0),
              length = 20,
              width = 2,
              height = 0.2,
              color = vector(1, 1, 1),
              opacity = 0.5)
#draw block1
block1 = box(length = 2,
             width = 2,
             height = 2,
             color = vector(1, 1, 1),
             opacity = 0.5)
#position block1 such that it rests on middle of board
block1.pos = incline.pos + vector(0, 0.5*block1.height, 0)

#create a parameter called block_vleocity to start the block1 from rest
block1.velocity = vector(0, 0, 0)

#draw a cylinder that represents a massless pulley with negligible axle friction
pulley = cylinder(axis=vector(0,0,1), radius = 0.5*block1.width, color= vector(0,1,0))

#reposition pulley to over the edge of the board
pulley.pos += vector(pulley.radius + 0.5*incline.length, 0, -0.25*incline.width)

#draw string1 connecting block1 1 to top edge of pulley
string1 = cylinder(radius = 0.1, color = vector(1, 1, 1), opacity=0.5)
string1.pos = pulley.pos + vector(0, pulley.radius, 0.5*mag(pulley.axis))
string1.axis = block1.pos + vector(0.5*block1.width, 0, 0) - string1.pos

#rotate the two objects about the z-axis (z-axis points out of page)
incline.rotate(angle = theta, axis = vector(0, 0, 1), origin = vector(0, 0, 0))
block1.rotate(angle = theta, axis = vector(0, 0, 1), origin = vector(0, 0, 0))
pulley.rotate(angle = theta, axis = vector(0, 0, 1), origin = vector(0, 0, 0))
string1.rotate(angle = theta, axis = vector(0, 0, 1), origin = vector(0, 0, 0)) 

#draw a hanging mass1 directly below the right edge of pulley
block2 = box(length = 2,
             width = 2,
             height = 2,
             color = vector(1, 1, 1),
             opacity = 0.5)
block2.pos = pulley.pos + vector(pulley.radius, - 0.5*incline.length, 0)

#draw string2 connecting block1 2 to right edge of pulley
string2 = cylinder(radius = 0.1, color = vector(1, 1, 1), opacity=0.5)
string2.pos = pulley.pos + vector(pulley.radius, 0, 0.5*mag(pulley.axis))
string2.axis = block2.pos + vector(0, 0.5*block2.height, 0) - string2.pos

#draw weight arrow
weight = vector(0, -mass1*g, 0)
weight_arrow = arrow(pos = block1.pos,
                     axis = scale_arrow*weight,
                     color = vector(0, 1, 0))
#draw normal force arrow
normal_mag = mass1*g*cos(theta)
normal = normal_mag*vector(-sin(theta), cos(theta), 0)
normal_arrow = arrow(pos = block1.pos,
                     axis = scale_arrow*normal,
                     color = vector(1, 0, 1))

#compute critical angle in RADIANS
theta_critical = atan(mu_s)

#critical mass for mass2
mass_critl = mass1*g*sin(theta) - mass2*g
mass_crith = mass1*g*sin(theta) - mass2*g
print'lower', mass_critl, 'high', mass_crith

if mass1*g*sin(theta) < mass2*g:
    print'+ a vec'
    fric_mag = mu_k*normal_mag #compute magnitude of fric
    fric = fric_mag*vector(cos(theta), sin(theta), 0) #make fric a vector
    fric_arrow = arrow(pos = block1.pos, #draw fric arrow
                       axis = scale_arrow*fric,
                       color = vector(0, 0.4, 1))
    F_net = normal + weight + fric #determine net force vector
    accel = -F_net/mass1 #determine a (Newton's 2nd)
    accel_arrow = arrow(pos = vector(-5,5,0), #draw accel arrow
                        axis = scale_arrow*accel,
                        color=vector(1, 0, 0))
    accel_display = mag(accel)
    ##accel_label = text(text='a='+accel_display+'m/s^2', #display accel
    ##color=vector(1, 0, 0),
    ##pos = vector(-6,5,0),
    ##height = 0.5)
    t = 0
    dt = 0.01
    sim_speed = 1
    while abs(block1.pos.x) < incline.length/2*cos(theta):
        rate(sim_speed/dt) #set the frames per second displayed
        block1.velocity += accel*dt #update block1 velocity
        block1.pos += block1.velocity*dt #update block1 position
        string1.axis = block1.pos + vector(0.5*block1.width*cos(theta), 0.5*block1.height*sin(theta), 0) - string1.pos
        weight_arrow.pos = block1.pos #keep arrows with block1
        fric_arrow.pos = block1.pos
        normal_arrow.pos = block1.pos
        t += dt #increment the time
elif mass1*g*sin(theta) > mass2*g:
    print'- a vec'
    fric_mag = mu_k*normal_mag #compute magnitude of fric
    fric = fric_mag*vector(cos(theta), sin(theta), 0) #make fric a vector
    fric_arrow = arrow(pos = block1.pos, #draw fric arrow
    axis = scale_arrow*fric,
                       color = vector(0, 0.4, 1))
    F_net = normal + weight + fric #determine net force vector
    accel = F_net/mass1 #determine a (Newton's 2nd)
    accel_arrow = arrow(pos = vector(-5,5,0), #draw accel arrow
                        axis = scale_arrow*accel,
                        color=vector(1, 0, 0))
    accel_display = mag(accel)
    ##accel_label = text(text='a='+accel_display+'m/s^2', #display accel
    ##color=vector(1, 0, 0),
    ##pos = vector(-6,5,0),
    ##height = 0.5)
    t = 0
    dt = 0.01
    sim_speed = 1
    while abs(block1.pos.x) < incline.length/2*cos(theta):
        rate(sim_speed/dt) #set the frames per second displayed
        block1.velocity += accel*dt #update block1 velocity
        block1.pos += block1.velocity*dt #update block1 position
        string1.axis = block1.pos + vector(0.5*block1.width*cos(theta), 0.5*block1.height*sin(theta), 0) - string1.pos
        weight_arrow.pos = block1.pos #keep arrows with block1
        fric_arrow.pos = block1.pos
        normal_arrow.pos = block1.pos
        t += dt #increment the time
else:
    print'equal'

print'Theta Crit=',theta_critical,', a=', accel_display # <----python=bad
