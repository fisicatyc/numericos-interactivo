# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
    Description: class ncentraldiff defines a set of numerical methods based on
    finite differences with no central step - forward or backward. Capable of
    aproximating derivatives at a given point inside an interval including 
    endpoints. Precision is highly dependant on interval size, bigger intervals
    lead to highter truncation errors. Minor error types are of h^2 order. First
    non centered aproximations for derivatives are a fast way to obtain a good
    aproximation, but second non centerd aproximations provides more accurate
    results but increase computation demand. Other aproximations use high order
    Taylor series expansion.
    
    Method inputs: n - integer - Defines number of n+1 elements in list.
                   lowerlimit - float - first term of interval.
                   upperlimit - float - last term of interval.
                   function - function type object - evaluates f(x) at x.
                   
    Method output: diff_array - list - list of derivated values in (a,b).              
    
    call sequence example: function = lambda x: 0.5*x**3+5*x*2+6*x+6.33;
                           ncentraldiff.snfirstderv(4, 0, 2, function);
                  
    Dependencies: None.
    
    Version: 1.2 for Python 3.4
    
    Definitions are taken from:
        Jaan Kiusalaasr. "Numerical Methods in Engineering With Python 3".
        3th ed. "Chapter 5 - Numerical Differentiation". 
        Cambridge University Press. 2013. PP. 185 - 186.
        
    Author: J.J. Cadavid - SFTC - EAFIT University.
    Contact: jcadav22@eafit.edu.co
    
    Date: 28/12/2014.
"""

def snfirstderv(n, lowerlimit, upperlimit, function):

    test = lambda: None;
    if isinstance(function,type(test)) == 0:
        raise Exception("function must be lambda object-type");
        
# Initilization
    diff_array = [0]*(n - 1);
    
# Assignations of spatial domain
    h = upperlimit-lowerlimit;
    x_array = [lowerlimit + x*h/n for x in range(n+1)];
                 
# Non centered expanded first Derivative approximation
    for i in range(n-2):
        diff_array[i] = (-function(x_array[i] + 2*h) + \
        4*function(x_array[i] + h) - 3*function(x_array[i]))/2*h;
    return(diff_array);
