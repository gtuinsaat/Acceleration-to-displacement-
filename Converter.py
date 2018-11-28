#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 20:39:38 2018

@author: seyhanokuyan
"""
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import scipy.integrate 

datafile_acc=pd.read_excel("19980627135553_0105.xlsx")#read your data file
data_acc=datafile_acc["N-S"]*0.01;#gal to m/s^2 convert units
acceleration = list(data_acc) #make data type as list
#velocity = [0]
time_step = 0.005# time step of ground motion data
N=5843;#number of total step
time = np.linspace(0.0, N*time_step, N) # duration vector 
velocity=scipy.integrate.cumtrapz(acceleration, x=time) #acceleration to velocity
displacement=scipy.integrate.cumtrapz(velocity, x=time[:-1]) #velocity to displacement
#for acc in acceleration:
#    velocity.append(velocity[-1] + acc * time)file:///C:/Users/casper/Desktop/WONG-ENERGY/analysis/pushover_4%25
#del velocity[0]


plt.plot(time[:-2], displacement)
plt.grid(True)
plt.xlim(0,30)
plt.ylim(-1,1)
plt.show()
