# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 18:47:58 2014

@author: Usuario
"""

def horner(x, *polynomial):
    """A function that implements the Horner Scheme for evaluating a
    polynomial of coefficients *polynomial in x."""
    result = 0
    for coefficient in polynomial:
        result = result * x + coefficient
    return result
    
res=horner(-2,*[2, -6, 2, -1])
print(res);