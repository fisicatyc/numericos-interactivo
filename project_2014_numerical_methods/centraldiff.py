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

class centraldiff:
    
    """
        Method testlambda verifies whether or not function is a lambda object
        type. Generates an exception if is false. Method to be use only in
        own class.
    """
    
    def __testlambda(function):
        test = lambda: None;
        if isinstance(function,type(test)) == 0:
            raise Exception("function must be lambda object-type");
    """
        Method getarray generates a list of equally spaced elements to be
        derivated. Number of divisions are set by n parameter.
    """
    def __getarray(n, lowerlimit, upperlimit):
        
        h = upperlimit-lowerlimit;
        x_array = [x*h/n for x in range(n)];
        x_array.remove(x_array[0]);
        return x_array, h;
        
    """
        FCDA or First Centered Difference Aproximation, calculates the first
        derivative in the interval. Dependencies: testlambda, getarray.
    """
    def FCDA(n, lowerlimit, upperlimit, function):
        
        centraldiff.__testlambda(function);
        diff_array = [0]*(n - 1);             
        x_array, h = centraldiff.__getarray(n, lowerlimit, upperlimit);
        
        for i in range(n-2):
            diff_array[i] = (function(x_array[i] + h) - \
                            function(x_array[i] - h))/2*h;
        return(diff_array);
        
    """
        SCDA or Second Centered Difference Aproximation, calculates the second
        derivative in the interval. Dependencies: testlambda, getarray.
    """
    def SCDA(n, lowerlimit, upperlimit, function):
        
        centraldiff.__testlambda(function);
        diff_array = [0]*(n - 1);             
        x_array, h = centraldiff.__getarray(n, lowerlimit, upperlimit);
        
        for i in range(n-2):
            diff_array[i] = (function(x_array[i] + h) - \
                            2*function(x_array[i]) + \
                            function(x_array[i] - h))/h**2;
        return(diff_array);
        
    """
        TCDA or Third Centered Difference Aproximation, calculates the third
        derivative in the interval. Dependencies: testlambda, getarray.
    """        
    def TCDA(n, lowerlimit, upperlimit, function):
        
        centraldiff.__testlambda(function);
        diff_array = [0]*(n - 1);             
        x_array, h = centraldiff.__getarray(n, lowerlimit, upperlimit);
        
        for i in range(n-2):
            diff_array[i] = (function(x_array[i] + 2*h) - \
                            2*function(x_array[i] + h) + \
                            2*function(x_array[i] - h) - \
                            function(x_array[i] - 2*h))/2*h**3;
        return(diff_array);
        
    """
        QCDA or Fourth Centered Difference Aproximation, calculates the fourth
        derivative in the interval. Dependencies: testlambda, getarray.
    """             
    def QCDA(n, lowerlimit, upperlimit, function):
        
        centraldiff.__testlambda(function);
        diff_array = [0]*(n - 1);             
        x_array, h = centraldiff.__getarray(n, lowerlimit, upperlimit);
        
        for i in range(n-2):
            diff_array[i] = (function(x_array[i] + 2*h) - \
                            4*function(x_array[i] + h) + \
                            6*function(x_array[i]) - \
                            4*function(x_array[i] - h) + \
                            function(x_array[i] - 2*h))/h**4;
        return(diff_array);