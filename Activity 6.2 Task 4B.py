# Activity 6.2: Task 4
# File: Activity 6.2 Task 4B.py
# Date: 02-10-26
# By: Kayleigh Loge
# Electronic Signature
# Kayleigh Loge
# Develop a Python Program to compute the heat transfer rate
# ChatGPT was used to help (I was super confused)
# include libraries 
import math
#get inports from user
house_T_F = float(input("Please enter the temprature inside the house (in (F)): "))
outside_T_F = float(input("Please enter the temprature outside the house (in(F)): "))
area_ft2 = float(input("Please enter the surface area of the house (in(ft^2)): "))
height_ft = float(input("Please enter the height of the house (in(ft)): "))
# converts
house_T_C = (house_T_F - 32) * 5 / 9
outside_T_C = (outside_T_F - 32) * 5 / 9
house_T_K = house_T_C + 273.15
outside_T_K = outside_T_C + 273.15
area_m2 = area_ft2 * 0.092903
height_m = height_ft * 0.3048
# constants
g = 9.81
k = 0.25
n = 1.217e-5
Pr = 0.7
# thermal expansion coefficient 
beta = 1 / outside_T_K
# rayleigh number
Ra = (g * beta * (house_T_K - outside_T_K) * height_m**3 * Pr) / n**2
# nusselt number
n =0.59 * Ra**0.25
# heat-transfer rate
q = h * area_m2 * (house_T_K - outside_T_K)
# display results
print(f"Heat transfer rate: {q:.2f} W")
