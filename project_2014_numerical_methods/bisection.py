# -*- coding: utf-8 -*-
"""
bisection.py is a function that calculates the roots of a polinomial function
using the bisection numerical method.

inputs= rf ; raw function, string of the form a*x+b
        a ; left range interval
        b ; right range interval
        n ; number of iterations
        t ; tolerance of calculation
        
output= x ; the aproximated value of x such that f(x)=0

version: 1.01 for python 2.7

fast_Code: bisection(('6*x-6'),-5,6,200,0.005);
    
author: JJ.Cadavid - SFTC - EAFIT University
date: 24/08/2014.
"""
import parser
import sys

def bisection(f,a,b,n,t):

# Input Verification    
    list_sze = len(aprx_list);
    test = lambda: None;
    if isinstance(polynm,type(test)) == 0:
        raise Exception("polynm must be lambda object-type");
    if list_sze != 3:
        raise Exception("Approximation needs 3 initial points");
		
# Initial Assignation		
    fa=f(a); #f(a) interval eval
    fb=f(b); #f(b) interval eval
    if ((fa*fb)>0): #Both images must cross the x-axis, a way to check is with sign
        raise Exception("[a,b] Interval does not cross the x-axis");
    fp=10;
    i=0;
	
# Main loop
    while (abs(fp)>t):
        x=a+(b-a)/2;    #Aproximation Calculation - changes every iteration
        fp=eval(f);
        print("f(p)={}".format(fp));
        if(fa*fp)>0:
            a=x;
        else:
            b=x;
        if(i>n):
            print("p={}".format(x));
            raise Exception("Tolerance not met by set iterations");
        i=i+1
    print("p={}".format(x));
    return(x);