from visual import *
#angle of block in DEGREES
angle_degrees = 35
#convert angle to RADIANS
theta = radians(angle_degrees)

#static and kinetic coefficients
#note: code will only produce reasonable results when mu_k < mu_s
mu_s = 0.5
mu_k = 0.3

#initialize mass and magnitude of freefall acceleration
g = 9.8
mass = 1.0

#create a scale factor which is useful for drawing arrows
#by adjusting the scale factor, you can draw the arrows larger or smaller
#this is useful if the arrows are really huge or really small
scale_arrow = 0.5

#draw a horizontal board
incline = box(pos = vector(0, 0, 0),
              length = 20,
              width = 2,
              height = 0.2,
              color = vector(1, 1, 1),
              opacity = 0.5)
#draw block
block = box(length = 1,
            width = 1,
            height = 1,
            color = vector(1, 1, 1),
            opacity = 0.5)
#position block such that it rest on board 3/4 from the left end
block.pos = incline.pos + vector(incline.length/4, block.height/2, 0)
#create a parameter called block_vleocity to start the block from rest
block.velocity = vector(0, 0, 0)

#rotate the two objects about the z-axis (z-axis points out of page)
incline.rotate(angle = theta, axis = vector(0, 0, 1), origin = vector(0, 0, 0))
block.rotate(angle = theta, axis = vector(0, 0, 1), origin = vector(0, 0, 0))

#draw weight arrow
weight = vector(0, -mass*g, 0)
weight_arrow = arrow(pos = block.pos,
                     axis = scale_arrow*weight,
                     color = vector(0, 1, 0))
#draw normal force arrow
normal_mag = mass*g*cos(theta)
normal = normal_mag*vector(-sin(theta), cos(theta), 0)
normal_arrow = arrow(pos = block.pos,
                     axis = scale_arrow*normal,
                     color = vector(1, 0, 1))

#compute critical angle in RADIANS
theta_critical = atan(mu_s)

#if theta > theta_critical, slipping should occur...use mu_k
if theta > theta_critical:
    fric_mag = mu_k*normal_mag                     #compute magnitude of fric
    fric = fric_mag*vector(cos(theta), sin(theta), 0) #make fric a vectortor
    fric_arrow = arrow(pos = block.pos,            #draw fric arrow
                       axis = scale_arrow*fric,
                       color = vector(0, 0.4, 1))
    F_net = normal + weight + fric                 #determine net force vectortor
    accel = F_net/mass                             #determine a (Newton's 2nd)
    accel_arrow = arrow(pos = vector(-5,5,0),         #draw accel arrow
                        axis = scale_arrow*accel,
                        color=vector(1, 0, 0))
    accel_display = mag(accel)
##    accel_label = text(text='a=' + accel_display + 'm/s^2', #display accel
##                       color=vector(1, 0, 0),
##                       pos = vector(-6,5,0),
##                       height = 0.5)
    t = 0
    dt = 0.01
    sim_speed = 1
    while abs(block.pos.x) < incline.length/2*cos(theta):
        rate(sim_speed/dt)              #set the frames per second displayed
        block.velocity += accel*dt      #update block velocity
        block.pos += block.velocity*dt  #update block position
        weight_arrow.pos = block.pos    #keep arrows with block
        fric_arrow.pos = block.pos
        normal_arrow.pos = block.pos
        t += dt                         #increment the time
else:
    fric_mag = mass*g*sin(theta)                   #compute fric magnitudue
    fric = fric_mag*vector(cos(theta), sin(theta), 0) #compute fric vectortor
    fric_arrow = arrow(pos = block.pos,            #draw fric arrow
                       axis = scale_arrow*fric,
                       color = vector(0, 0.4, 1))
##    accel_label = text(text='a=0',                 #write "a=0" on the screen
##                       color=vector(1, 0, 0),
##                       pos = vector(-5,5,0),
##                       height = 0.5)
