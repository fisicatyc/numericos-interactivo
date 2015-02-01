# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
    Description: function compmidtrule is part of the Composite Integration
    Techniques and can be thought as an upgrated version of midpoint rule
    integration technique that aproximates a defined integal evaluated in [a,b]
    with better presicion in larger intervals. It's truncation error is of order
    h^2 and defined by a second order derivative.
    
    Inputs: lowerlimit - float - defines first limit of integration.
            upperlimit - float - defines last limit of integration.
            redc - integer - even integer that defines subintervals.
            function - function type object - evaluates f(x) at x.
            
    Outputs: integ - float - defined integral aproximation
    
    Example line: compmidtrule(-3.15, 6.2, 8, (lambda x: 2*x**3 + 4.3));
                  
    Dependencies: None.
    
    Version: 1.2 for Python 3.4
    
    Definitions were taken from:
        Richard L. Burden, J. Douglas Faires. "Numerical Analysis" 9th ed.
        "Chapter 4 - Numerical Differentiation and Integration". 
        Cengage Learning. 2010. pp: 203 - 209.
        
    Author: J.J. Cadavid - SFTC - EAFIT University.
    Contact: jcadav22@eafit.edu.co
    
    Date: 28/12/2014.
"""

def compmidtrule(lowerlimit, upperlimit, redc, function):
    
# Initial input error verification
    if redc % 2 != 0:
        raise Exception('Reduced inverval - redc- must be an even integer');
        
    test = lambda: None;
    if isinstance(function,type(test)) == 0:
        raise Exception("function must be lambda object-type");
        
# Zero initializing         
    sumf = 0;
    x_array = [0]*(redc + 1)
    
# Grid spacing
    h = (upperlimit - lowerlimit)/(redc + 2);
    
# Integration Domain Generation
    for i in range(-1, redc - 1):
        x_array[i] = lowerlimit + (i + 1)*h;

# Main loop - sum aproximation
    for j in range(0, (redc/2)):
        sumf = sumf + function(x_array[2*j]);
        
    integ = 2*h*sumf;
    
    return(integ);