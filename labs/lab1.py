from visual import *
offsetScale = 10
offset = -vector(offsetScale, offsetScale)
line_x=cylinder(pos = offset, axis= (-offset.x*2,0), radius =.1)
line_x=cylinder(pos = offset, axis= (0,-offset.y*2), radius =.1)

ball = sphere (pos = offset, color = color.orange, radius = 0.5)
velInit = vector(10, 10)
ball.vel = velInit
outputs = 100
deltat = float(1.0/outputs) #specify sigs by inputting a point for sig
print(deltat)
t = 0
a = vector(0,-9.8)
simSpeed = 1

while ball.pos.y > offset.y or t == 0:
    rate(simSpeed/deltat)
    #print("Y Pos: % .3f, T: % .3f" %(ball.pos.y-offset.y, t))
    print("% .3f,% .3f" %(ball.pos.y-offset.y, t))
    ball.vel = (ball.vel + a*deltat)
    ball.pos = (ball.pos+ball.vel*deltat)
    t = t + deltat
