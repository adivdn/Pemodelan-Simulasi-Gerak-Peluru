# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:05:52 2020

@author: ADIV
"""

import matplotlib.pyplot as plt
import numpy
import math

arrayOfXNumerik = []
arrayOfYNumerik = []
arrayOfNumerik = []

arrayOfXAnalitik = []
arrayOfYAnalitik = []
arrayOfAnalitik = []


speed = float(input('Masukkan Kecepatan : '))
degree = float(input('Masukkan Sudut Kemiringan : '))
timedelta = float(input('Masukkan Time Delta : '))

Sin = round(math.sin(math.radians(degree)),2)
Cos = math.cos(math.radians(degree))



g = 9.8
time = float((2 * speed * Sin) / g)

atas = float(math.pow(speed,2) * math.pow(Sin,2))
bawah = float(2*g)

hMax = float(atas/bawah)

tTop = speed * Sin / g

R = speed * Cos * time

g = g * -1

positionXNumerik = 0
positionYNumerik = 0

positionXAnalitik = 0
positionYAnalitik = 0

speedNumerikX = float(speed * Cos)
speedNumerikY = float(speed * Sin)

speedAnalitikX = float(speed * Cos)
speedAnalitikY = float(speed * Sin)

arrayOfXNumerik.append(positionXNumerik)
arrayOfYNumerik.append(positionYNumerik)

arrayOfXAnalitik.append(positionXAnalitik)
arrayOfYAnalitik.append(positionYAnalitik)

for t in numpy.arange(0,time+timedelta,timedelta):
    speedNumerikY = speedNumerikY + (g * timedelta)
    positionXNumerik = positionXNumerik + (speedNumerikX * timedelta)
    positionYNumerik = positionYNumerik + (speedNumerikY * timedelta)
    arrayOfXNumerik.append(positionXNumerik)
    arrayOfYNumerik.append(positionYNumerik)
    if positionYNumerik < 0:
        print(t)
        break


for t in numpy.arange(0,time+timedelta,timedelta):
    
     positionXAnalitik = speedAnalitikX * t
     arrayOfXAnalitik.append(positionXAnalitik)
  

for t in numpy.arange(0,time+timedelta,timedelta):

    positionYAnalitik = speedAnalitikY * t + (0.5 * g * math.pow(t,2))
    arrayOfYAnalitik.append(positionYAnalitik)
    if positionYAnalitik < 0:
        print(t)
        break
    
    
print('Waktu Total : ',time)
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(arrayOfXAnalitik,arrayOfYAnalitik,'r-o')
plt.plot(arrayOfXNumerik,arrayOfYNumerik,'b')
plt.legend(['Analitik','Numerik'],loc = 'best')
plt.ylim(0,hMax)
print ('Jarak Maksimum : ',R)
print ('Tinggi Maksimum : ',hMax)
plt.show()


