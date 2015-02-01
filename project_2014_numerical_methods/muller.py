# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
    Description: function muller is a multiple polynomial root finding algorithm.
    Due to method limitations functions with roots that are not simple
    (Multiplicity > 1), Müller's technique is limitated. For that purpose use
    high order quadrature or adaptative root finding algorithms. Since polynomial
    roots are unique, all functions of this type, even those with complex roots,
    can be easily obtained with Müller's algorithm. This program request
    three seeds in which the roots are located, from there all roots there are
    obatained. This program will be traslated to polyroot class to make a
    selection between  Müller's and Horner's technique whether or not there are
    complex roots. If tolerance is not met the program raises an exception.
    
    Inputs: polynm - lambda object type - polynomial function to be evaluated.
            aprx_list - list object - list containing three seeds.
            tol - float - error tolerance in roots.
            iters - integer - Positive value providing the number of loops.
            
    Outputs: p - float - Polynomial root obtained from seeds.
    
    Example code: [];
                  
    Dependencies: None.
    
    Version: 1.2 for Python 3.4
    
    Definitions are taken from:
        Richard L. Burden, J. Douglas Faires. "Numerical Analysis" 9th ed.
        "Chapter 2 - Solutions of Equations in One Variable". 
        Cengage Learning. 2010. pp: 97 - 98.
        
    Author: J.J. Cadavid - SFTC - EAFIT University.
    Contact: jcadav22@eafit.edu.co
    
    Date: 24/12/2014.
"""

def muller(polynm, aprx_list, tol, iters):
    
# Input Verification    
    list_sze = len(aprx_list);
    test = lambda: None;
    if isinstance(polynm,type(test)) == 0:
        raise Exception("polynm must be lambda object-type");
    if list_sze != 3:
        raise Exception("Approximation needs 3 initial points");
        
# Initial value assignations        
    p0 = aprx_list[0];
    p1 = aprx_list[1];
    p2 = aprx_list[2];
    h1 = (p1 - p0);
    h2 = (p2 - p1);
    delta1 = (polynm(p1)-polynm(p0))/h1;
    delta2 = (polynm(p2)-polynm(p1))/h2;
    d=(delta2 - delta1)/(h2 + h1);

# Main loop - root finder
    i=1;
    while i < iters:
        b = delta2 + h2*d;
        D = (b**2 - 4.0*polynm(p2)*d)**(1.0/2.0);
        if abs(b - D) < abs(b + D):
            E = b + D;
        else:
            E = b - D;
        h = -2.0*polynm(p2)/E;
        p = aprx_list[2] + h;
        if abs(h) < tol:
            return(p);
        p0 = p1;
        p1 = p2;
        p2 = p;
        h1 = (p1 - p0);
        h2 = (p2 - p1);
        delta1 = (polynm(p1)-polynm(p0))/h1;
        delta2 = (polynm(p2)-polynm(p1))/h2;
        d=(delta2 - delta1)/(h2 + h1);
        i=i+1;
    raise Exception("Iterations completed, yet toleration not met.");