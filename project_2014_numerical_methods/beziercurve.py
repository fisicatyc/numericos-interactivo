# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
    Description: function beziercurve generates an interpolation parametric
    curve using a third order Hermite polynomial and a pair of nodes and
    guidelines. Endpoint slope is calculated with the slope of lines
    tangent to them. Therefore no second or first analytic derivative 
    forms of curve is needed a priori. The fast computation of this interpolant
    allows an interactive way to generate curves. Spatial coordinates are
    the only requiremnt for calculation.
    
    Inputs: endpoints - list object - includes 4 float values for nodes.
            leftguide - list object - includes 4 float values for left node.
            rightguide - list object - includes 4 float values for right node.
            n - integer - optional parameter defines number n+1 elements of list.
            
    Output: beziercoeff - list object - Bezier cofficients of polynomial.
    
    Example code: endpoints = [[3.2, 2.4], [3.6, 0.4]];
                  leftguide = [[2.8, 7.5], [5.3, 6.4]];
                  rightguide = [[8.3, 7.5], [1.6, 2.4]];
                  beziercurve (endpoints, leftguide, rightguide, n=10);
                  
    Dependencies: None.
    
    Version: 1.3 for Python 3.4
    
    Definition and structure were taken from:
        Richard L. Burden, J. Douglas Faires. "Numerical Analysis" 9th ed.
        "Chapter 3 - Interpolation and Polynomial Approximation". 
        Cengage Learning. 2010. pp: 166 - 169.
        
    Author: J.J. Cadavid - SFTC - EAFIT University.
    Contact: jcadav22@eafit.edu.co
    
    Date: 27/12/2014.
"""

def beziercurve (endpoints, leftguide, rightguide, n=10):
    
# Zero initializing - list type
    a0 = [0]*n;
    a1 = a0;
    a2 = a1;
    a3 = a2;
    b0 = a3;
    b1 = b0;
    b2 = b1;
    b3 = b2;   
    
# Initial value assignation
    nestedlist = [endpoints, leftguide, rightguide]; # Nested list for compact variable usage.
    coorlist = [ [ 0 for i in range(2) ] for j in range(3) ];
    
# Array generation for equal separated values
    for i in range(len(nestedlist) - 1):
        for j in range(len(nestedlist[1]) - 1):
            if nestedlist[i][j][0] < nestedlist[i][j][1]: # upper and lower assignation due to negative values.
                lower = nestedlist[i][j][0];
                upper = nestedlist[i][j][1];
            else:
                lower = nestedlist[i][j][1];
                upper = nestedlist[i][j][0];
            coorlist[i][j] = [lower + x*(upper-lower)/n for x in range(n+1)]; # generation of x, y values inside interval.
            
# Main loop - Interpolant coefficients    
    for k in range(n):
        a0[k] = coorlist[0][0][k]; # subscripts at level 3: [0] x value,[1] y value.
        b0[k] = coorlist[0][1][k];
        a1[k] = 3*(coorlist[1][0][k] - coorlist[0][0][k]); # subscripts at level 2: [0] initial endpoint list,[1] final endpoint list.
        b1[k] = 3*(coorlist[1][1][k] - coorlist[0][1][k]);
        a2[k] = 3*(coorlist[0][0][k] + coorlist[2][0][k + 1] - 2*(coorlist[1][0][k])); 
        b2[k] = 3*(coorlist[0][1][k] + coorlist[2][1][k + 1] - 2*(coorlist[1][1][k]));
        a3[k] = coorlist[0][0][k + 1] - coorlist[0][0][k] + 3*(coorlist[1][0][k]) \
                - 3*(coorlist[2][0][k + 1]); # subscripts at level 1: [0] endpoint list,[1] leftguide endpoints, [2] rightline endpoint.
        b3[k] = coorlist[0][1][k + 1] - coorlist[0][1][k] + 3*(coorlist[1][1][k]) \
                - 3*(coorlist[2][1][k + 1]);
    
    beziercoeff = [a0, a1, a2, a3, b0, b1, b2, b3];
    return beziercoeff;