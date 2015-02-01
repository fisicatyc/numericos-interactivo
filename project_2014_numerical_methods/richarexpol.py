# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
    Description: function richarexpol is a small method that applies Richardson
    Extrapolation. This technique is one of the keystones in Advance Numerical
    Methods. Extrapolation allows to increase the presicion of a numerical 
    result whitout increasing data nodes, whenever space grid size, h, is involve.
    For this program, extrapolation receives 2 approximations of a value dependent
    on h, and by setting the correct order p from analytical truncation error
    high accurate results can be obtained.
    
    Inputs: P - integer - Non negative integer setting the order of correction term
            firstaprx - float - first approximation of an h dependent value;
            secondprx - float - second approximation of an h dependent value;
                   
    Method Outputs: G - float - High accurate result
    
    Example code: [];
                  
    Dependencies: None.
    
    Version: 1.0 for Python 3.4
    
    Definitions are taken from:
        Jaan Kiusalaasr. "Numerical Methods in Engineering With Python 3".
        3th ed. "Chapter 5 - Numerical Differentiation". 
        Cambridge University Press. 2013. PP. 188 - 189.
        
    Author: J.J. Cadavid - SFTC - EAFIT University.
    Contact: jcadav22@eafit.edu.co
    
    Date: 28/12/2014.
"""

def richarexpol(p, firstaprx, secondprx):
    
    G = (2**p*firstaprx - secondprx)/(2**p - 1);
    return(G);