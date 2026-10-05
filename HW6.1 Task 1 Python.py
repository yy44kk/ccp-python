# HW 6.2 Python 1: Task 1
# File: HW6.1 Task 1 Python.py
# Date: 04-10-26
# By: Kayleigh Loge
# Electronic Signature 
# Kayleigh Loge
# Compute and output the Work done (W)
# include libraries
import math
# get inputs from users
m = float(input("Please enter the mass of the object (in(kg)): ")
vi = float(input("Please enter the intial velocity (in(m/s)): ")
vf = float(input("Please enter the final velocity (in(m/s)): ")
# compute results
W = 0.5 * m * (vf**2-vi**2)
# display results
print("Work done =", W, "J")
