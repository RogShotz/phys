from visual import *

#Creating backgroud plane (box object)
background = box(size = vector(4.5, 4.5, .01),
                  color = color.blue)


#Simulation Variables
offset = 1
posInit = vector(0, 2) #radius
ball = sphere (pos = posInit, color = color.white, radius = 0.1)
velInit = vector(0, 0)
ball.vel = velInit

#creating Lines
line_y1 = cylinder(pos = vector(posInit.x - 2*ball.radius, -offset),
                   axis= (0, offset),
                   radius =.01,
                   color = color.red)
line_y2 = cylinder(pos = vector(posInit.x - 2*ball.radius, -offset + offset),
                   axis= (0, offset),
                   radius =.01,
                   color = color.blue)
line_y3 = cylinder(pos = vector(posInit.x - 2*ball.radius, -offset + 2 * offset),
                   axis= (0, offset),
                   radius =.01,
                   color = color.green)
line_x = cylinder(pos = vector(-offset, 0),
                  axis= (2 * offset, 0),
                  radius =.01,
                  color = color.black)

deltat = .01
t = 0
a_0 = vector(0 , -9.8)
a = vector(0, -9.8)
Tao = -30               #only seems to have a noticable change between # and #
inc = 1                 #the amount we will subract from Tao for each iteration
yDefault = line_x.radius #default y position that nothing should go below
replay = false          #restarts the animation(resets the ball position to origin)
inputDriven = false     #allows for input from user
simActive = true        #Helps to stop while loop when the ball is at the bottem
simSpeed = .5

while ball.pos.y >= yDefault and simActive == true:
    rate(simSpeed/deltat)

    #print to screen
    print("Y:% .3f, t:% .3f, T:% .3f, a: % .3f ,v: % .3f" %((ball.pos.y),
                                                    t,
                                                    Tao,
                                                    a.y,
                                                    ball.vel.y))

    #Updates the balls 'ACCELERATION'
    a = a_0 * math.e**(-t/Tao)

    #Updates the balls 'VELOCITY'
    ball.vel = (velInit - (Tao * a * (math.e**(-t/Tao) - 1)))
    
    #Updates the balls 'POSITION' and makes sure it does not go below the line
    if (posInit + velInit * t + (a * Tao * (Tao * math.e**(-t/Tao) + t - Tao))) < yDefault:
        ball.pos.y = yDefault
        if replay == false:
            simActive = false
    else:
        ball.pos = (posInit + velInit * t + (a * Tao * (Tao * math.e**(-t/Tao) + t - Tao)))

    #Updates 'TIME'
    t = t + deltat


    if replay == true and ball.pos.y == yDefault:        
        #reset ball information
        ball.pos = posInit
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
        
        
        
