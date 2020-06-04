# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math

def myquad(Ain, Bin, Cin):
    if Bin**2 < 4.0*Ain*Cin:
        print("complex results not allowed")
        return(0, 0)
    else: 
        x1 = (-Bin + math.sqrt(Bin**2 - 4.0*Ain*Cin))/(Ain*2)
        x2 = (-Bin - math.sqrt(Bin**2 - 4.0*Ain*Cin))/(Ain*2)
        return (x1, x2)
    
(out1, out2) = myquad(2.0, 1.0, 2.0)
print(out1, out2)