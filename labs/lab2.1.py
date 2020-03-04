from visual import *

##=======To Do List========##

scene.width = 700
scene.height = 800


#angle of block1 in DEGREES
angle_degrees = 90

#convert angle to RADIANS
theta = radians(angle_degrees)

#static and kinetic coefficients
#note: code will only produce reasonable results when mu_k < mu_s
mu_s = 0.5
mu_k = 0.3

#initialize mass and magnitude of freefall acceleration
g = 9.8
mass1 = 1.0 # hockey puck
mass2 = 2.0 # prediction

#Draw a background
background = box(pos = vector(0, 0, -5),
                 length = 35,
                 width = .01,
                 height = 25,
                 color = color.black)

#useful for drawing arrows with mags
scale_arrow = 0.25

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
             opacity = 0.3)

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
             opacity = 0.3)
block2.pos = pulley.pos + vector(pulley.radius, - 0.5*incline.length, 0)
block2_init_pos = pulley.pos + vector(pulley.radius, - 0.5*incline.length, 0)

#block 2 velocity
block2.velocity = vector(0, 0, 0)

#draw string2 connecting block2 to right edge of pulley
string2 = cylinder(radius = 0.1, color = vector(1, 1, 1), opacity=0.5)
string2.pos = pulley.pos + vector(pulley.radius, 0, 0.5*mag(pulley.axis))
string2.axis = block2.pos + vector(0, 0.5*block2.height, 0) - string2.pos

#draw mass1 weight arrow
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

#draw mass2 wieght arrow (mass2*g)
m2_weight_arrow = arrow(pos = block2.pos,
                     axis = scale_arrow*vector(0, -mass2*g, 0),
                     color = vector(0, 1, 0)) 

#compute critical mass for mass2
small_critical_mass = mass1*(sin(theta) - mu_s*cos(theta))
large_critical_mass = mass1*(sin(theta) + mu_s*cos(theta))


##=====Pseudocode======
##if     m_2 == m_1*sin(theta)                          then m_1 is STILL and there is no friction
##elif   m_2 <  m_1*(sin(theta) + mu_s*cos(theta))      then m_1 is STILL and friction is UP the incline
##elif   m_2 >  m_1*(sin(theta) - mu_s*cos(theta))      then m_1 is STILL and friction is DOWN the incline
##elif   m_2 >  m_1*(sin(theta) + mu_s*cos(theta))      then m_1 is accelerating UP the incline and friction is DOWN the incline
##elif   m_2 <  m_1*(sin(theta) - mu_s*cos(theta))      then m_1 is acceleratiing DOWN the incline and friction is UP the incline


#=========Static Friction and Zero Friction (zero acceleration)===================
if mass2 >= small_critical_mass and mass2 <= large_critical_mass:
    T_mag = mass2*g                                             #OUTPUT: solving for tension
    T = T_mag*vector(cos(theta), sin(theta), 0)
    
    if mass2 == mass1*sin(theta):                               #compute magnitude of fric
        print ("no friction")
        fric_mag = 0
        fric = vector(0, 0, 0)
    else:
        fric_mag = mu_s*normal_mag
        if mass2 > mass1*sin(theta):                            #friction is DOWN the incline
            fric = -fric_mag*vector(cos(theta), sin(theta), 0)  #make fric a vector
            print ("friction DOWN the incline")
        else:                                                   #friction is UP the incline
            fric = fric_mag*vector(cos(theta), sin(theta), 0)   #make fric a vector
            print ("friction UP the incline")
    
    fric_arrow = arrow(pos = block1.pos,                                                            #draw fric arrow
                       axis = scale_arrow*fric,
                       color = vector(0, 0.4, 1))

    
    F_net_x = T_mag*cos(theta) - normal_mag*sin(theta) - fric_mag*cos(theta)                        #determine net force vector
    F_net_y = T_mag*sin(theta) + normal_mag*cos(theta) - fric_mag*sin(theta) - mass1*g
    F_net = vector(F_net_x, F_net_y, 0)                                                             #make F_net a vector
    accel = vector(0, 0, 0)
    accel_mag = mag(accel)
    
    accel_arrow = arrow(pos = vector(-5,5,0),                                                       #draw accel arrow
                        axis = scale_arrow*accel,
                        color=vector(1, 0, 0))

    accel_text = text(text = '0',
                      align = 'center', depth = -0.3,
                      color = color.blue,
                      pos = accel_arrow.pos)

    #draw tension arrow
    tension_arrow = arrow(pos = block2.pos,
                     axis = scale_arrow*vector(0, T_mag, 0),
                     color = vector(1, 1, 0))
    
    
    t = 0
    dt = 0.01
    sim_speed = 1

    
    #Outputs: T, a, f, n
    #acceleration is 0 when you are in this part of the code
    print "Given:, M_1 =", mass1, ", M_2 =", mass2, ", theta =", angle_degrees, ", mu_s =", mu_s, ", mu_k =", mu_k, ", g =", g
    print "looking for:, Tension =", T_mag, ", Acceleration =", 0, ", friction =", fric_mag, ", Normal =", normal_mag
        
#=========Kinetic Friction ===================

else:
    accel_mag = 0                                               #determined in if statement below
    fric_mag = mu_k*normal_mag
    fric = vector( 0, 0, 0)
    accel = vector(0, 0, 0)
    accel_2 = accel
    
    if mass2 > mass1*(sin(theta) + mu_k*cos(theta)):                                        #friction is DOWN the incline
        fric = -fric_mag*vector(cos(theta), sin(theta), 0)                                  #make fric a vector
        print ("friction DOWN the incline")
        accel_mag = g*(mass2 - mass1*(sin(theta) + mu_k*cos(theta))) / (mass1 + mass2)      
        accel = accel_mag*vector(cos(theta), sin(theta), 0)                                 #acceleration is Up the incline (used for block1)
        print ("accelerate Up the incline")
        accel_2.y = -accel_mag
        
    elif mass2 < mass1*(sin(theta) + mu_k*cos(theta)):                                      #friction is UP the incline
        fric = fric_mag*vector(cos(theta), sin(theta), 0)                                   #make fric a vector
        print ("friction UP the incline")
        accel_mag = g*(mass1*(sin(theta) - mu_k*cos(theta)) - mass2) / (mass1 + mass2)
        accel = -accel_mag*vector(cos(theta), sin(theta), 0)                                #acceleration is DOWN the incline (used for block1)
        print ("accelerate DOWN the incline")
        accel_2.y = accel_mag

    T_mag = mass2*(g + accel_2.y)                                           #OUTPUT: solving for tension
    T = T_mag*vector(cos(theta), sin(theta), 0)

    ##Draw the arrows!
    fric_arrow = arrow(pos = block1.pos,                    #draw fric arrow
                       axis = scale_arrow*fric,
                       color = vector(0, 0.4, 1))
    
    accel_arrow = arrow(pos = vector(-3,5,0),               #draw accel arrow
                        axis = scale_arrow*accel,
                        color=vector(1, 0, 0))

    
    tension_arrow = arrow(pos = string2.pos,
                     axis = scale_arrow*vector(0, T_mag, 0),
                     color = vector(1, 1, 0))

    ##Draw the text! Got it working!
    accel_text = text(text = 'Acceleration: %s' % str(round(accel_mag, 3)),
                      align = 'left', depth = -0.3,
                      color = accel_arrow.color,
                      pos = vector(-10, 10, 0),
                      height = 0.75)
    tension_text = text(text = 'Tension: %s' % str(round(T_mag, 3)),
                      align = 'left', depth = -0.3,
                      color = accel_arrow.color,
                      pos = vector(-10, 9, 0),
                      height = 0.75)
    normal_text = text(text = 'Normal: %s' % str(round(normal_mag, 3)),
                      align = 'left', depth = -0.3,
                      color = accel_arrow.color,
                      pos = vector(-10, 8, 0),
                      height = 0.75)
    fric_text = text(text = 'Friction: %s' % str(round(fric_mag, 3)),
                      align = 'left', depth = -0.3,
                      color = accel_arrow.color,
                      pos = vector(-10, 7, 0),
                      height = 0.75)

    t = 0
    dt = 0.01
    sim_speed = 1
    
    #Outputs: T, a, f, n
    print "Given:, M_1 =", mass1, ", M_2 =", mass2, ", theta =", angle_degrees, ", mu_s =", mu_s, ", mu_k =", mu_k, ", g =", g
    print "looking for:, Tension =", T_mag, ", Acceleration =", accel_mag, ", friction =", fric_mag, ", Normal =", normal_mag
    print "Critical mass for mass 2: ,", small_critical_mass, large_critical_mass
    Y = abs(incline.length/2*sin(theta))
    X = abs(incline.length/2*cos(theta))
    disp = 0
    
    #while loop abs(block1.pos.x) < incline.length/2*cos(theta)
    ##=====pseudocode=====
    ##if theta > 45 or theta < -45 use: y
    ##else: use y
    moving = true
    while (moving):
        #Code that keeps block 1 on the incline
        if angle_degrees < -45 or angle_degrees > 45:
            if block1.pos.y > Y or block1.pos.y < -Y:
                moving = false
        else:
            if block1.pos.x > X or block1.pos.x < -X:
                moving = false
        rate(sim_speed/dt)                                  #set the frames per second displayed
        block1.velocity += accel*dt                         #update block1 velocity
        block1.pos += block1.velocity*dt                    #update block1 position
        block2.velocity += accel_2*dt                       #update block2 velocity
        block2.pos += block2.velocity*dt                    #update block2 position
        string1.axis = block1.pos + vector(0.5*block1.width*cos(theta),
                                               0.5*block1.height*sin(theta),
                                               0) - string1.pos
        string2.axis = block2.pos + vector(0, 0.5*block2.height, 0) - string2.pos        
        weight_arrow.pos = block1.pos                       #keep arrows with block1
        fric_arrow.pos = block1.pos
        normal_arrow.pos = block1.pos
        m2_weight_arrow.pos = block2.pos
        tension_arrow.pos = block2.pos
        t += dt #increment the time
        
