#field.py
from math import *
esp0 = 9.954E-12
mu0 = 4*pi*1E-7

def electric_field(q:float,r:float)->float:
    E = q/(4*pi*esp0*r**2)
    return E
def magnetic_field(L:float,s:float)->float:
    B = mu0*L/(2*pi*s)
    return B
