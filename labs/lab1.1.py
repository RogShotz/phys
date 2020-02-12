from visual import *


#Simulation Variables
offsetScale = 1
offset = -vector(offsetScale, offsetScale)
posInit = vector(0, -offset.y)

#Scene
ball = sphere (pos = posInit, color = color.blue, radius = 0.15)
line_y=cylinder(pos = -vector(-offset.x, -offset.y + ball.radius + .05),
                axis= (0,-offset.y*2),
                radius =.05)
line_x=cylinder(pos = -vector(offset.x/offset.x, -offset.y + ball.radius + line_y.radius),
                axis= (-offset.x*2,0), radius =.05)
background = box(size = vector(4.5, 4.5, .01),
                  color = color.green)

velInit = vector(0, 0)
ball.vel = velInit

deltat = .01
t = 0
a_0 = vector(0 , -9.8)
a = vector(0, -9.8)
Tao = .225              #only seems to have a noticable change between # and #
inc = 1                 #the amount we will subract from Tao for each iteration
yDefault = offset.y     #default y position that nothing should go below
replay = false          #restarts the animation(resets the ball position to origin)
inputDriven = false     #allows for input from user
simActive = true        #Helps to stop while loop when the ball is at the bottem
simSpeed = .2

while t < 10:
    rate(1)
    t += 1

t=0
while ball.pos.y >= yDefault and simActive == true:
    rate(simSpeed/deltat)

    #print to screen
    print("Y:% .3f, t:% .3f, T:% .3f, a: % .3f ,v: % .3f" %((ball.pos.y-offset.y),
                                                    t,
                                                    Tao,
                                                    a.y,
                                                    ball.vel.y))
    #When it approximately hits terminal vel
    if (a.y > -0.5):
        ball.color = color.red

    
    #Updates the balls 'ACCELERATION'
    a = a_0 * math.e**(-t/Tao)

    #Updates the balls 'VELOCITY'
    ball.vel += a*deltat
    
    #Updates the balls 'POSITION' and makes sure it does not go below the line
    if (posInit + velInit * t + (a * Tao * (Tao * math.e**(-t/Tao) + t - Tao))) < yDefault:
        ball.pos.y = yDefault
        if replay == false:
            simActive = false
    else:
        ball.pos += ball.vel * deltat

    #Updates 'TIME'
    t = t + deltat


    if replay == true and (ball.pos.y - yDefault) < .001:     
        t=0
        while t < 10:
            rate(1)
            t = t + 1
        t=0
        #reset ball information
        ball.pos = posInit
        ball.vel = vector(0, 0)
        a = a_0
        #Input driven
        if inputDriven == true:
            userInput = input("Tao: ")
            if userInput == "":
                replay = false
            else:
                Tao = userInput
        else: #Incrementing Tao
            Tao = Tao - 0
        
        
        
