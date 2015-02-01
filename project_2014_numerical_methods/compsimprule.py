# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
    Description: function compsimprule is part of the Composite Integration
    Techniques and can be thought as an upgrated version of Simpson rule
    integration technique that aproximates a defined integal evaluated in [a,b]
    with better presicion in larger intervals. It's truncation error is of order
    h^4 and defined by a fourth order derivative. Presicion is slighly better
    than Composite midpoint rule and so is the best option when minimizing
    number of computations. Is also known to be an all-purpose quadrature algorithm.
    
    Inputs: lowerlimit - float - defines first limit of integration.
            upperlimit - float - defines last limit of integration.
            redc - integer - even integer that defines subintervals
            function - function type object - evaluates f(x) at x.
            
    Outputs: integ - float - defined integral aproximation
    
    Example line: integ = compmidtrule(-3.15, 6.2, 8, (lambda x: 2*x**3 + 4.3));
                  
    Dependencies: None.
    
    Version: 1.2 for Python 3.4
    
    Definition and structure were taken from:
        Richard L. Burden, J. Douglas Faires. "Numerical Analysis" 9th ed.
        "Chapter 4 - Numerical Differentiation and Integration". 
        Cengage Learning. 2010. pp: 203 - 209.
        
    Author: J.J. Cadavid - SFTC - EAFIT University.
    Contact: jcadav22@eafit.edu.co
    
    Date: 28/12/2014.
"""

def compsimprule (lowerlimit, upperlimit, redc, function):

# Initial input error verification
    if redc % 2 != 0:
        raise Exception('Reduced inverval - redc- must be an even integer');
        
    test = lambda: None;
    if isinstance(function,type(test)) == 0:
        raise Exception("function must be lambda object-type");
        
# Initial assignation and zero initializing       
    h = (upperlimit - lowerlimit)/redc;
    XI0 = function(lowerlimit) + function(upperlimit);
    XI1 = 0;
    XI2 = 0;
    
# Integration Domain Generation    
    for i in range (1,(redc-1)):
        X = lowerlimit + i*h;
        
        if i % 2 == 0:
            XI2 = XI2 + function(X);
        else:
            XI1 = XI1 + function(X);
            
# Simpson standard rule for aproximation            
    XI = h*(XI0 + 2*XI2 + 4*XI1)/3;
    
    return(XI);