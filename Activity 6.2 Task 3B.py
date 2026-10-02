# Activity 6.2: Task 3
# File: Activity 6.2 Task 3B.py
# Date: 02-10-26
# By: Kayleigh Loge
# Electronic Signature
# Kayleigh Loge
#Develop a Python Program to compute the maximum allowable sound intensity
# Sound pressure level (SPL) 
# include libraries 
import math
# get inputs from user
SPL = 190
Pref = 1e-6
v = 1
# compute my results
P = Pref * 10**(SPL / 20)
I = P * v
# display results
print("Sound pressure:", P, "Pa")
print("Maximum sound intensity:", I, "W/m^2")
