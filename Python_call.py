
#import c types
from ctypes import *
import math
import numpy as np
import matplotlib.pylab as plt

Simulation_Libs = CDLL('./libhmwk7.so')

def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros

# big enough loop number to run 5 min
rand_num=100000000

step_time=1
step_radius=2
time_bin=(25/step_time)
radius_bin=(900/step_radius)
spec_prob = c_double(0.1)


time_dis = zerolistmaker(time_bin)
radius_dis = zerolistmaker(radius_bin)

# Initiallize the value
time = c_double(0.)
radius = c_double(0.)
itime=c_int(0)
iradius=c_int(0)

for i in range (0,rand_num):
	
	#Accumulate histagram for time-dependence photon
    Simulation_Libs.simulation(spec_prob,byref(time),byref(radius))
    itime = int (time.value*1000/step_time)
    if (itime < time_bin):
        time_dis[itime] = time_dis[itime] + 1
	
	#Accumulate histagram for radius-dependence photon
    Simulation_Libs.simulation(spec_prob,byref(time),byref(radius))
    iradius = int (radius.value*1000/step_radius)
    if (iradius < radius_bin):
       radius_dis[iradius] = radius_dis[iradius] + 1

#Calculate the percentage of photon
#set the x,y of plot
x1=np.linspace(0,25,time_bin)
x2=np.linspace(0,900,radius_bin)
y1=np.zeros(time_bin)
y2=np.zeros(radius_bin)
for i in range(0,time_bin):
	y1[i]=float(time_dis[i])/rand_num
for i in range(0,radius_bin):
	y2[i]=float(radius_dis[i])/rand_num

#plot 2 figure
plt.plot(x1,y1)
plt.xlabel('Times(ns)')
plt.ylabel('Average percent detected cherenkov photons')
plt.title('Detected photons versus time')
plt.show()
plt.savefig("hmwk7_plt1.jpg")

plt.plot(x2,y2)
plt.xlabel('Enterring radius of muon(mm)')
plt.ylabel('Average percent detected cherenkov photons')
plt.title('Detected photons per muon')
plt.show()
plt.savefig("hmwk7_plt2.jpg")
