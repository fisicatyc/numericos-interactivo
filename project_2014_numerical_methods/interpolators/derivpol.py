# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
    Description: function derivpol calculates the derivatives of interpolated
    data. A good choice to create interpolant are the cubic splines they are
    used in this program. Clamped and Natural Splines used information of
    first and second derivatives in knots, by applying algebraic manipulation
    expressions to calculate derivates are obtained.
    
    Inputs: domainlist - list object - list whose elements are x domain data.
            imagelist - list object - list whose elements are y domain data.
            evalpnt - list object - point to evaluate the derivatives.
            
    Outputs: firstderiv, secndderiv - Automatic tuple of lists of derivatives.
    
    Example code: domainlist = [0 + (x*(10-0)/5)*x**2 for x in range(6)];
                  imagelist = [0 + (x*(10-0)/5)*x**4 for x in range(6)];
                  evalpnt = 5.4;
                  fd, sd = derivpol(domainlist, imagelist, evalpnt);
                  
    Dependencies: cubicSpline.py - Jaan Kiusalaasr - 2013.
    
    Version: 1.1 for Python 3.4
    
    Definition and structure were taken from:
        Jaan Kiusalaasr. "Numerical Methods in Engineering With Python 3".
        3th ed. "Chapter 5 - Numerical Differentiation". 
        Cambridge University Press. 2013. PP. 191 - 195.
        
    Author: J.J. Cadavid - SFTC - EAFIT University.
    Contact: jcadav22@eafit.edu.co
    
    Date: 28/12/2014.
"""

from cubicSpline import curvatures;

def derivpol(domainlist, imagelist, evalpnt):
    
# Initial input error verification   
    if len(domainlist) != len(imagelist):
        raise Exception("Not equal number of nodes and images");

# Interpolation generation        
    k = curvatures(domainlist, imagelist);
    knots_length= len(k);

# Zero Initializing
    firstderiv = [0]*knots_length;
    secndderiv = firstderiv;
    
# Main loop - derivative in the knots
    for i in range(knots_length - 1):
        
        firstderiv[i] = k[i]/6*((3*(evalpnt - domainlist[i+1])**2)/ \
                            (domainlist[i] - domainlist[i+1]) \
                            - (domainlist[i] - domainlist[i+1])) - \
                        k[i+1]/6*((3*(evalpnt - domainlist[i])**2)/ \
                            (domainlist[i] - domainlist[i+1]) \
                            - (domainlist[i] - domainlist[i+1])) + \
                        ((imagelist[i] - imagelist[i+1])/ \
                        (domainlist[i] - domainlist[i+1]));
                        
        secndderiv[i] = k[i]*((evalpnt - domainlist[i+1])/ \
                            (domainlist[i] - domainlist[i+1])) - \
                        k[i+1]*((evalpnt - domainlist[i])/ \
                            (domainlist[i] - domainlist[i+1]));

    return firstderiv, secndderiv;                                