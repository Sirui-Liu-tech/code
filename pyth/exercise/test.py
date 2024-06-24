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
import numpy as np
J0 = 1
J1 = 1/3
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
                temp.append([random.choice([-1,1]),random.choice([-1,1])])
                points.append((30+j*a/2.0+i*a,30+(math.sqrt(3)/2)*j*a))
                points.append((30+j*a/2.0+i*a+a/2.0,30+(math.sqrt(3)/2)*j*a+(math.sqrt(3)/6)*a))
        m.append(temp)

plt.ion()
figure, ax = plt.subplots()
lines, = ax.plot([], [])
ax.set_autoscaley_on(True)
ax.grid()
xdata = [0]
ydata = [0]
lines.set_xdata(xdata)
lines.set_ydata(ydata)
ax.relim()
ax.autoscale_view()
figure.canvas.draw()
figure.canvas.flush_events()

runn = True

def calcu(tem,echo,time,m):
        y = []
        for kkk in range(time):
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
                y.append(magnetic(m))
        return sum(y[100:])/len(y[100:])

time = int(input('time'))

for tt in np.arange(0.01,2000,50):
        xdata.append(tt)
        ydata.append(calcu(tt,echo,time,m))
        lines.set_xdata(xdata)
        lines.set_ydata(ydata)
        ax.relim()
        ax.autoscale_view()
        figure.canvas.draw()
        figure.canvas.flush_events()

plt.savefig('mag_temprature.jpg')