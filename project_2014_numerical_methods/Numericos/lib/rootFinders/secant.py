# -*- coding: utf-8 -*-
"""
secant.py finds the root of a function using the Secant method given the
    initial aproximations p1 and p0 so that the root is a number between them

Inputs: f - Function in terms of 'x'
        p0,p1 - Initial aproximations
        tol - Tolerance
        n - maximum number of iterations
        
Outputs: Aproximate solution X or message of failure

Quick Code: secant('math.cos(x)-x',0.5,math.pi/4,5*10**-8,20)
        
Version: 1.0

Author: Sebastián Castaño - SFTC - EAFIT University   
 
"""
import sys
import math

def secant(f,p0,p1,tol,n):
    x=p0
    q0=eval(f)  #Evaulates the function at p0
    x=p1
    q1=eval(f)  #Evaulates the function at p1
    for num in range(1,n+1):    #Makes a set number of iterations
        p=p1-q1*(p1-p0)/(q1-q0)
        if(abs(p-p1)<tol):  #Verifies if the tolerance is met
            sys.exit("Solution = {}".format(p))
        #Update values for next iteration
        p0=p1
        q0=q1
        p1=p
        x=p
        q1=eval(f)
    sys.exit("The method failed after {} iterations. The tolerance was not met"
    .format(n))