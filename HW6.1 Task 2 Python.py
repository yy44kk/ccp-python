# HW 6.2 Python 1: Task 2
# File: HW6.1 Task 2 Python.py
# Date: 04-10-26
# By: Kayleigh Loge
# Electronic Signature 
# Kayleigh Loge
# Calculates the monthly payment for a
# loan based on user inputs for the loan amount, annual interest rate (in percentage), and the loan
# term in years
# include libraries
import math
# get inputs from users
P = float(input("Please enter the loan amount (principal): ")
A_R = float(input("Please enter the annual interest rate (in(%)): ")
y = float(input("Please enter the loan term (in(years): ")
# calculate results          
r = A_R / (12 * 100)
n = y * 12
M = (P * r (1 + r) ** n) / ((1 + r) ** n - 1)
# display results
print(f"Monthly payment: ${M: .2f}")
