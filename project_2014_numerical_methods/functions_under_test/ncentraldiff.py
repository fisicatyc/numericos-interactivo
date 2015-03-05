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
    
    call sequence example: ncentraldiff.nfirstderv(4, 0, 2, (lambda x: 4*sin(x)**2));
                  
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

class ncentraldiff:
    
    def __testlambda(function):
        test = lambda: None;
        if isinstance(function,type(test)) == 0:
            raise Exception("function must be lambda object-type");
    
    def __getarray(n, lowerlimit, upperlimit):
        
        h = upperlimit-lowerlimit;
        x_array = [lowerlimit + x*h/n for x in range(n+1)];
        return x_array, h;

    def nfirstderv(n, lowerlimit, upperlimit, function):

        ncentraldiff.__testlambda(function);
        diff_array = [0]*(n - 1);             
        x_array, h = ncentraldiff.nfirstderv(n, lowerlimit, upperlimit);

        for i in range(n-2):
            diff_array[i] = (function(x_array[i] + h) - function(h))/h;
        return(diff_array);        
        
    def nsecondderv(n, lowerlimit, upperlimit, function):
        
        ncentraldiff.__testlambda(function);
        diff_array = [0]*(n - 1);             
        x_array, h = ncentraldiff.nfirstderv(n, lowerlimit, upperlimit);

        for i in range(n-2):
            diff_array[i] = (function(x_array[i] + 2*h) - \
                            2*function(x_array[i] + h) + function(x_array[i]))/h**2;
        return(diff_array);
        
    def snfirstderv(n, lowerlimit, upperlimit, function):
        
        ncentraldiff.__testlambda(function);
        diff_array = [0]*(n - 1);             
        x_array, h = ncentraldiff.nfirstderv(n, lowerlimit, upperlimit);

        for i in range(n-2):
            diff_array[i] = (-function(x_array[i] + 2*h) + \
            4*function(x_array[i] + h) - 3*function(x_array[i]))/2*h;
        return(diff_array);