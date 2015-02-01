# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
    Description: function clampspline generates an interpolant of third order 
    polynomial. Uses knot information of second derivatives in the first and last
    knot. The coefficients are solved using the tridiagonal linear system 
    vectorial equation AX = B by recursion in the strictly diagonally dominant 
    matrix A.
    
    Inputs: domainpnt - list object - list whose elements are x domain data.
            imagepnt - list object - list whose elements are y domain data.
            fstderpnt - list object - second derivative knot information, 2 elements.
            
    Outputs: a, b, c, d - Automatic tuple of lists - interpolant coefficients.
    
    Example code: domainpnt = [(x*(10-0)/5)*x**2 for x in range(6)];
                  imagepnt = [(x*(10-0)/5)*x**(2*3**0.5) for x in range(6)];
                  fstderpnt = [];
                  
    Dependencies: None.
    
    Version: 1.1 for Python 3.4
    
    Definition and structure were taken from:
        Richard L. Burden, J. Douglas Faires. "Numerical Analysis" 9th ed.
        "Chapter 3 - Interpolation and Polynomial Approximation". 
        Cengage Learning. 2010. pp: 145 - 149.
        
    Author: J.J. Cadavid - SFTC - EAFIT University.
    Contact: jcadav22@eafit.edu.co
    
    Date: 27/12/2014.
"""

def natspline (domainpnt, imagepnt, dervendpnt):

# Input value checking  
    dm_sze = len(domainpnt);
    if dm_sze != len(imagepnt):
        raise Exception("Not equal number of nodes and images");
    
    if len(dervendpnt) != 2:
         raise Exception("Insufficient endpoints data");
    else:
         if dervendpnt[0] != 0 or  dervendpnt[1] != 0:
             raise Exception("Second derivative criteria not met in interval");
             
# Initializing and initial assignation        
    n = dm_sze - 1;
    h = [0]*n;
    a = imagepnt;
    l = h;
    u = l;
    z = u;
    c = z;
    b = c;
    d = b;
    l[0] = 1;
    l[n] = 1;
    
    for i in range(n - 1):
         h[i] = domainpnt[i + 1] - domainpnt[i];

# Main loop - Coefficient calculations by tridiagonal linear system solving         
    for i in range(1,(n - 1)):
         a[i] = 3/h[i]*(a[i + 1] - a[i]) - 3/h[i-1]*(a[i] - a[i-1]);
         l[i] = 2*(domainpnt[i + 1] - domainpnt[i - 1]) - (h[i - 1]*u[i - 1]);
         u[i] = h[i]/l[i];
         z[i] = (a[i] - h[i - 1]*z[i - 1])/l[i];
         
    for j in range ((n - 1), -1, -1):
        c[j] = z[j] - u[j]*c[j + 1];
        b[j] = (a[j + 1] - a[j])/h[j] - h[j]*(c[j + 1] + 2*c[j])/3;
        d[j] = (c[j + 1] - c[j])/(3*h[j]);
    
    return a, b, c, d;