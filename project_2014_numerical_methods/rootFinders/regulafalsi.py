# -*- coding: utf-8 -*-
"""

regulafalsi.py finds the root of a function continuous in an interval [p0,p1]
    where f(p0) and f(p1) have opposite signs

Inputs: f- Function in terms of x
        p0,p1 - Interval
        tol - Tolerance
        n - Maximum number of itarations
        
Outputs: Aproximate solution X or message of failure

Quick Code: fixedpoint('(1.0/2.0)*((10.0-x**3)**(1.0/2.0))',1.5,3,10**-8)
        
Version: 1.0

Author: Sebastián Castaño y Felipe Lopez - SFTC - EAFIT University

"""
import sys
import math

def regulafalsi(f,p0,p1,tol,n):
    x=p0
    q0=eval(f)  #Evaulates the function at p0
    x=p1
    q1=eval(f)  #Evaulates the function at p1
    for num in range(1,n+1):    #Makes a set number of iterations
        p=p1-q1*(p1-p0)/(q1-q0)
        if(abs(p-p1)<tol):  #Verifies if the tolerance is met
            sys.exit("Solution = {}".format(p))
        x=p
        q=eval(f)
        if(p*p1<0):
            p0=p1
            q0=q1
        #Update values for next iteration
        p1=p
        q1=q
    sys.exit("The method failed after {} iterations. The tolerance was not met"
    .format(n))