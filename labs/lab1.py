from visual import *
#I changed the code for 1d motion. Jorstad said we are over complicating it.

#====Notes=====
#When Tao is 2.1 the ball will keep going up but very slowly
#~ a_init = 10
#~ v_init = < 0, 0>
#find terminal velocity

#Creating backgroud plane (boxa object)
background = box(size = vector(2.25, 2.25, .01),
                  color = color.blue)

offset = .5
pos_init = vector(0, 1)

ball = sphere (pos = pos_init, color = color.white, radius = 0.05)
#line_y.x = line_y.x - ball.radius * 3  #Moved the line over to the left
velInit = vector(0, 0)
ball.vel = velInit

#creating Lines
#line_y = cylinder(pos = vector(pos_init.x - 0.1, -offset), axis= (0, 1), radius =.01, color = color.black)
line_x = cylinder(pos = vector(-offset, -offset), axis= (2 * offset, 0), radius =.01, color = color.black)

#arrow (pos=ball.pos, axis = velInit*.1, color = color.green)
deltat = .05
t = 0
a = vector(0,-10)
Tao = .1               #only seems to have a noticable change between # and #
inc = .1                #the amount we will subract from Tao for each iteration
yDefault = line_x.y + line_x.radius + ball.radius   #default y position that nothing should go below
simSpeed = 1            #Controlls the speed of the simulation
replay = false          #restarts the animation(resets the ball position to origin)
inputDriven = false     #allows for input from user

while ball.pos.y >= yDefault:
    rate(simSpeed/deltat)
    print("Y Position:% .3f, Time:% .3f, Tao:% .3f" %(ball.pos.y + offset,
                                                    t,
                                                    Tao))
    a = a * math.e**(-t/Tao)
    ball.vel = (ball.vel + a*deltat)

    #this makes sure it does go below the line
    if ball.pos.y + ball.vel.y*deltat < yDefault:
        ball.pos.y = yDefault
    else:
        ball.pos = (ball.pos+ball.vel*deltat)
        
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
            Tao = Tao - inc
        
        
        

