import math
# User inputs
v=float(input('Please enter the fluid velocity (mph)'))
l=float(input('Please enter the typical length (in)'))
u=float(input('Please enter the fluid viscoity (lb/(in*s))'))
p=float(input('Please enter the fluid density (lb/in^3)'))
v1=v*5280*12/(60*60)
re=p*v1*l/u
print('Reynolds number is {0}'. format(re))
