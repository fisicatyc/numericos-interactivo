# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
    Description: class centraldiff defines a set of numerical methods based on
    finite differences of central step. Capable of aproximating derivatives at
    a given point inside an interval. Central step does not evaluate derivatives
    at endpoints. Precision is highly dependant on interval size, bigger intervals
    lead to highter truncation errors. Minor error types are of h^2 order.
    Analitical errors can be calculated using fourth derivatives. Highter
    derivative orders can lead to high truncation errors, so results are likely
    to differ a lot from analytical results, especially with interpolated data.
   
    FCDA or First Centered Difference Aproximation, calculates the first
    derivative in the interval. Dependencies: testlambda, getarray.  
    
    Method inputs: n - integer - Defines number of n+1 elements in list.
                   lowerlimit - float - first term of interval.
                   upperlimit - float - last term of interval.
                   function - function type object - evaluates f(x) at x.
                   
    Method output: diff_array - list - list of derivated values in (a,b).              
    
    call sequence example: centraldiff.FCDA(4, 0, 2, (lambda x: 4*sin(x)**2));
                  
    Dependencies: None.
    
    Version: 1.2 for Python 3.4
    
    Definitions are taken from:
        Jaan Kiusalaasr. "Numerical Methods in Engineering With Python 3".
        3th ed. "Chapter 5 - Numerical Differentiation". 
        Cambridge University Press. 2013. PP. 183 - 185.
        
    Author: J.J. Cadavid - SFTC - EAFIT University.
    Contact: jcadav22@eafit.edu.co
    
    Date: 28/12/2014.
"""

def FCDA(n,lowerlimit, upperlimit, function, x, flag = False):
    test = lambda: None;
    if isinstance(function,type(test)) == 0:
        raise Exception("function must be lambda object-type");
     
    h = upperlimit-lowerlimit;
    hc = h/(n-1);
    
    if flag:
        arrayStart = lowerlimit;
        x_array = [arrayStart + hc*x for x in range(n)];
        diff_array = [0]*n;             
    
        for i in range(n):
            diff_array[i] = (function(x_array[i] + h) - \
                        function(x_array[i] - h))/2*h;
    else:
        diff_array = (function(x + h) - \
                        function(x - h))/2*h;
    return(diff_array);