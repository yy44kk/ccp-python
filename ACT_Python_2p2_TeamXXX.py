# Activity 9.2 Python 2: Task 2
# File: ACT_Python_2p2_TeamXXX.py
# Date: 14-10-26
# By: Kayleigh Loge
# Electronic Signature 
# Kayleigh Loge
# Use a nested conditional structure and relational and logical operators in Python to
# determine whether a solution is acidic, basic, or neutral based on the pH.
# include libraries
import math
# ask the user to enter the pH of a solution 
ph = float(input("Please enter the pH of the solution: "))
# determine whether the pH is valid and classify the solution 
if 0 <= ph <= 14:
  if ph < 7:
    print("The solution is acidic.")
  elif ph == 7:
    print("The solution is neutral.")
  if ph <= 14:
    print("The solution is basic.")
  else:
    print("The solution is not valid.")
