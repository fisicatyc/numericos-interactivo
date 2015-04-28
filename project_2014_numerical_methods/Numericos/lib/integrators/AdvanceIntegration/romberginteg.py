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
            subinterv - positive integer - Number of subintervals
            function - lambda object type - evaluates f(x) at x
            
    Outputs: R - list object - Romberg table - integration aproximation.
    
    Example code: R = romberginteg(-3.15, 6.2, 10, (lambda x: 2*x**3 + 4.3));
                  
    Dependencies: None.
    
    Version: 1.5 for Python 3.4
    
    Definition and structure were taken from:
        Richard L. Burden, J. Douglas Faires. "Numerical Analysis" 9th ed.
        "Chapter 4 - Numerical Differentiation and Integration". 
        Cengage Learning. 2010. pp: 213 - 218.
        
    Author: J.J. Cadavid - SFTC - EAFIT University.
    Contact: jcadav22@eafit.edu.co
    
    Date: 19/02/2015.
"""

def romberginteg(lowerlimit, upperlimit, subinterv, function):

# Input verification    
    test = lambda: None;
    if isinstance(function,type(test)) == 0:
        raise Exception("function must be lambda object-type");

# List of list assignation    
    R = [[ 0 for i in range(subinterv+1) ] for j in range(subinterv+1)];

# Spatial grid size
    h = (upperlimit - lowerlimit);

# First Seed Approximation
    R[0][0] = 0.5*h*(function(upperlimit) + function(lowerlimit));

# Main Loop -> Composite Trapezoide approx. -> Extrapolation
    for i in range(1, (subinterv + 1)):
        h = 0.5 * h;
        sumf = 0.0;
        for j in range( 1, 2**i, 2 ):
            sumf = sumf + function( lowerlimit + j * h );

        R[i][0] = (0.5 * R[i-1][0]) + (sumf * h); # Increase result accuracy 

        for k in range( 1, i + 1 ):
            R[i][k] = R[i][k-1] + ( R[i][k-1] - R[k-1][k-1] ) / ( 4**i - 1 )
        
    return(R);  
  