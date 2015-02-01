# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
    Description: function romberginteg computes an approximation of a defined
    integral in [a,b]. Romberg Integration uses other minor techniques to produce
    accurate results. First aproximations are obtain from one of the Newton-Cotes
    Formulas and then results are improve with extrapolation techniques. Then
    the process is done all over again on the subinterval section. Every loop
    grid size is half for better presicion improvement.
    
    Inputs: lowerlimit - float - First element in integration interval
            upperlimit - float - Last element in integration interval
            redc - integer - Number of subintervals
            function - lambda object type - evaluates f(x) at x
            
    Outputs: R - float - double integration aproximation.
    
    Example code: R = romberginteg(-3.15, 6.2, 8, (lambda x: 2*x**3 + 4.3));
                  
    Dependencies: None.
    
    Version: 1.1 for Python 3.4
    
    Definition and structure were taken from:
        Richard L. Burden, J. Douglas Faires. "Numerical Analysis" 9th ed.
        "Chapter 4 - Numerical Differentiation and Integration". 
        Cengage Learning. 2010. pp: 213 - 218.
        
    Author: J.J. Cadavid - SFTC - EAFIT University.
    Contact: jcadav22@eafit.edu.co
    
    Date: 29/12/2014.
"""

def romberginteg(lowerlimit, upperlimit, redc, function):
    
    test = lambda: None;
    if isinstance(function,type(test)) == 0:
        raise Exception("function must be lambda object-type");
    
    n = redc - 1;
    R = [[ 0 for i in range(n) ] for j in range(2)];
    h = (upperlimit - lowerlimit);
    R[0][0] = h/2*(function(upperlimit) + function(lowerlimit));
    
    sumf = 0;
    for i in range(2, (redc + 2)):
        for j in range(1, (2**(i - 2))):
            sumf = sumf + function(lowerlimit + (j - 0.5)*h);
            
        R[1][0] = 0.5*(R[0][0] + h*sumf);
        
        for k in range(2, i):
            R[1][k-1] = R[1][k-2] + (R[1][k-2] - R[0][k-2])/(4**(k-1) - 1);
        
        h = h/2;
        R[0] = R[1];
        
    return(R);        