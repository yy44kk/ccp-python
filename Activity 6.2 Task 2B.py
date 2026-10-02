# include libraries
import math
# get inputs from the user
v_mi_hr = float(input('Please enter the fluid velocity (in (mi/hr)): '))
l_in = float(input(' Please enter the typical lenght (in (in)):'))
u_lb_in_s = float(input(' Please enter the dynamic viscosity of the fluid (lb/(in*s)): '))
p_lb_in = float(inout(' Please enter the density of the fluid (in (lb/in³)): '))
# compute my results
v= v_mi_hr * 1609.344 / 3600
l= l_in * 0.0254
u= u_lb_in_s * 0.45359237 / 0.0254
p= p_lb_in * 0.45359237 / (0.0254 ** 3)
# display results
re = (p * v * l) / u
print(f"Reynolds number (re) = {Re:.2f}")
