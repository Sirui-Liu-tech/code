def chx(flag,x):
        if flag:
                if x + 1 <= xr-1:
                        return x+1
                else:
                        return 0
        else:
                if x - 1 >= 0:
                        return x-1
                else:
                        return xr-1

def hamiltonchange(x,y,z):
        global m,J0,J1
        currentspin = m[x][y][z]
        temp = 0
        if z == 0:
                temp += J0*(m[chx(False,x)][y][1] + m[x][y][1])*currentspin
                if y>0:
                        temp += J0*(m[x][y-1][1])*currentspin
        else:
                temp += 0*(m[chx(True,x)][y][0] + m[x][y][0])*currentspin
                if y<yr-1:
                        temp += J0*(m[x][y+1][0])*currentspin
        if J1:
                temp += J1*(m[chx(False,x)][y][z] + m[chx(True,x)][y][z])*currentspin
                if y > 0:
                        temp += J1*(m[x][y-1][z]+m[chx(True,x)][y-1][z])*currentspin
                if y < yr-1:
                        temp += J1*(m[x][y+1][z]+m[chx(False,x)][y+1][z])*currentspin
        return -temp

def magnetic(m):
        temp = 0
        for i in m:
                for j in i:
                        temp += sum(j)
        return temp
     
import math
import pygame
import random
from matplotlib import pyplot as plt
J0 = 1
J1 = 0
m = []
points = []
colorr = [(155,155,155),(255,0,0)]
a = float(input("length"))
xr,yr = map(int,input("row & column").split())
tem = float(input("temprature"))
echo = int(input('rate per time'))
for i in range(xr):
        temp = []
        for j in range(yr):
                temp.append([1,1])
                points.append((30+j*a/2.0+i*a,30+(math.sqrt(3)/2)*j*a))
                points.append((30+j*a/2.0+i*a+a/2.0,30+(math.sqrt(3)/2)*j*a+(math.sqrt(3)/6)*a))
        m.append(temp)


pygame.init()
screen = pygame.display.set_mode((1500, 900), 0, 32)
for point in points:
        pygame.draw.circle(screen,(155,155,155),point, 10)

plt.ion()
figure, ax = plt.subplots()
lines, = ax.plot([], [])
ax.set_autoscaley_on(True)
ax.grid()
xdata = [0]
ydata = [magnetic(m)]
lines.set_xdata(xdata)
lines.set_ydata(ydata)
ax.relim()
ax.autoscale_view()
figure.canvas.draw()
figure.canvas.flush_events()

runn = True
while runn:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        runn = False
                for k in range(echo):
                        i = random.randint(0, xr-1)
                        j = random.randint(1, yr-1)
                        l = random.randint(0,1)
                        deltaH = hamiltonchange(i,j,l)
                        test = random.random()
                        if test < math.exp(-deltaH/tem):
                                m[i][j][l] = - m[i][j][l]
                                if i == 0:
                                        m[xr-1][j][l] = - m[xr-1][j][l]
                                elif i == xr-1:
                                        m[0][j][l] = - m[0][j][l]
                xdata.append(xdata[-1]+echo)
                ydata.append(magnetic(m))
                lines.set_xdata(xdata)
                lines.set_ydata(ydata)
                ax.relim()
                ax.autoscale_view()
                figure.canvas.draw()
                figure.canvas.flush_events()
                for i in range(xr):
                        for j in range(yr):
                                pygame.draw.circle(screen,colorr[(m[i][j][0]+1)//2],(30+j*a/2.0+i*a,30+(math.sqrt(3)/2)*j*a), 15)
                                pygame.draw.circle(screen,colorr[(m[i][j][1]+1)//2],(30+j*a/2.0+i*a+a/2.0,30+(math.sqrt(3)/2)*j*a+(math.sqrt(3)/6)*a), 15)

        pygame.display.update()
pygame.quit()