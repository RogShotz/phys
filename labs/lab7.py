from vpython import *

m_rod = 1  # mass of rod
L = 1  # length of support cable and Rod
g = -9.8
scale = .01
m_mass1 = 1  # mass 1 mass
x = .05  # 0 < x < 1
y = sqrt(L ** 2 - x ** 2)
thetat = atan(y / x)  # theta of tension

tG = gcurve(color=color.cyan)  # tension plot
rG = gcurve(color=color.green)  # reaction plot

wall = box(color=color.gray(0.5), pos=vec(0, 0, 0), length=.1, height=1.5, width=1)
wall.pos.x -= wall.length / 2  # Offset for animation and so everything can start at 0 as origin
rod = cylinder(color=color.magenta, radius=.025, pos=vec(0, 0, 0), axis=vec(L, 0, 0))  # Rod
cable = cylinder(color=color.gray(0.5), radius=0.0125, pos=vec(0, y, 0), axis=vec(x, -y, 0))  # Support cable
mass_1 = box(color=color.orange, pos=vec(L, -.25, 0), length=.07, height=.07, width=.07)  # Mass
mass_cable = cylinder(color=color.gray(0.5), radius=0.0125, pos=vec(L, 0, 0),
                      axis=vec(0, mass_1.pos.y, 0))  # Cable from rod to mass

# Force Vec Inits
f_yRod = m_rod * g  # force vector of rod only in y
f_rod = arrow(pos=vec(L / 2, 0, 0), axis=vec(0, f_yRod, 0) * scale, color=color.red,
              shaftwidth=0.05)
f_yMass1 = m_mass1 * g  # force vector of hanging mass only in y
f_Mass1 = arrow(pos=mass_1.pos, axis=vec(0, f_yMass1, 0) * scale, color=color.green,
                shaftwidth=0.05)
t_1 = (L ** 2 * m_mass1 + (m_rod / 2)) * g / (x * y)  # tension
t_x = t_1 * cos(thetat)
t_y = t_1 * sin(thetat)
f_tVec = arrow(pos=cable.pos + cable.axis, axis=vec(0, 0, 0) * scale, color=color.cyan,
               shaftwidth=0.05)
f_tVec.axis = vec(t_x, -t_y, 0) * scale

f_reactX = -t_1 * cos(thetat)
f_reactY = (m_mass1 + m_rod) * g - (L / x) * (m_mass1 + m_rod / 2) * g
f_react = arrow(pos=vec(0, 0, 0), axis=vec(f_reactX, -f_reactY, 0) * scale, color=color.green,
                shaftwidth=0.05)

while x <= .95:
    rate(10)
    t_1 = (L ** 2 * m_mass1 + (m_rod / 2)) * g / (x * y)  # updating tension
    t_x = t_1 * cos(thetat)
    t_y = t_1 * sin(thetat)
    f_tVec.pos = cable.pos + cable.axis
    f_tVec.axis = vec(t_x, -t_y, 0) * scale

    f_reactX = -t_1 * cos(thetat)  # updating reaction
    f_reactY = (m_mass1 + m_rod) * g - (L / x) * (m_mass1 + m_rod / 2) * g
    f_react.axis = vec(f_reactX, -f_reactY, 0) * scale

    cable.pos.y = y  # cable position update
    cable.axis = vec(x, -y, 0)

    x += .01
    y = sqrt(L ** 2 - x ** 2)
    thetat = atan(y / x)
    tG.plot(x, -t_1)
    rG.plot(x, sqrt(f_reactX ** 2 + f_reactY ** 2))
