from vpython import *

#Creating backgroud plane (box object)
background = box(size = vector(4.5, 4.5, .01),
                  color = color.blue)


#Simpulation Variables
offset = 1
pos_init = vector(0, 2)
ball = sphere (pos = vector(0, 1), color = color.white, radius = 0.1)
velInit = vector(0, 0)
ball.vel = velInit

#creating Lines
line_y1 = cylinder(pos = vector(pos_init.x - 2*ball.radius, -offset),
                   axis= (0, offset),
                   radius =.01,
                   color = color.red)
line_y2 = cylinder(pos = vector(pos_init.x - 2*ball.radius, -offset + offset),
                   axis= (0, offset),
                   radius =.01,
                   color = color.blue)
line_y3 = cylinder(pos = vector(pos_init.x - 2*ball.radius, -offset + 2 * offset),
                   axis= (0, offset),
                   radius =.01,
                   color = color.green)
line_x = cylinder(pos = vector(-offset, -offset - .01),
                  axis= (2 * offset, 0),
                  radius =.01,
                  color = color.black)

deltat = .01
t = 0
a_0 = vector(0 , -9.8)
a = vector(0, -9.8)
Tao = -1000              #only seems to have a noticable change between # and #
inc = .1                #the amount we will subract from Tao for each iteration
yDefault = line_x.y + line_x.radius + ball.radius   #default y position that nothing should go below
replay = false          #restarts the animation(resets the ball position to origin)
inputDriven = false     #allows for input from user
simActive = true        #Helps to stop while loop when the ball is at the bottem
simSpeed = 1

while ball.pos.y >= yDefault and simActive == true:
    rate(simSpeed/deltat)

    #print to screen
    print("Y Position:% .3f, Time:% .3f, Tao:% .3f, a: % .3f ,V: % .3f" %((ball.pos.y - line_x.pos.y + line_x.radius),
                                                    t,
                                                    Tao,
                                                    a.y,
                                                    ball.vel.y))

    #Updates the balls 'ACCELERATION'
    a = a_0 * math.e**(-t/Tao)

    #Updates the balls 'VELOCITY'
    ball.vel = (ball.vel + a*deltat)
    
    #Updates the balls 'POSITION' and makes sure it does not go below the line
    if ball.pos.y + ball.vel.y*deltat < yDefault:
        ball.pos.y = yDefault
        if replay == false:
            simActive = false
    else:
        ball.pos = (ball.pos+ball.vel*deltat)

    #Updates 'TIME'
    t = t + deltat


    if replay == true and ball.pos.y == yDefault:        
        #reset ball information
        ball.pos = pos_init
        ball.vel = velInit
        ball.pos.y = 0
        t = 0
        a = vector(0, -10)

        #Input driven
        if inputDriven == true:
            userInput = input("Tao: ")
            if userInput == "":
                replay = false
            else:
                Tao = userInput
        else: #Incrementing Tao
            Tao = Tao - 0
        
        
        
