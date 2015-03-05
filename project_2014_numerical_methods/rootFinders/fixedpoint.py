# -*- coding: utf-8 -*-
"""

fixedpont.py finds the root of a function using the fixed point method given the
    initial aproximations p0.

Inputs: g - Fixed point function with the form x=g(x) obtained from f(x)=0
        p0 - Initial aproximation
        tol - Tolerance
        n - Maximum number of itarations
        
Outputs: Aproximate solution X or message of failure

Quick Code: fixedpoint('(1.0/2.0)*((10.0-x**3)**(1.0/2.0))',1.5,3,10**-8)
        
Version: 1.0

Author: Sebastián Castaño y Felipe Lopez - SFTC - EAFIT University

"""
import sys
import math

def fixedpoint(g,p0,tol,n):
    for num in range(1,n+1):    #Makes a set number of iterations
        x=p0
        p1=eval(g)  #Evaulates the function at p0
        if(abs(p1-p0)<tol):  #Verifies if the tolerance is met
            sys.exit("Solution = {}".format(p1))
        #Update value for the next iteration
        p0=p1
    sys.exit("The method failed after {} iterations. The tolerance was not met"
    .format(n))
        
