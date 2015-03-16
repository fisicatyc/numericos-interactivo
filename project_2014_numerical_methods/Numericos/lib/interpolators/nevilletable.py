# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
    Description: function nevilletable computes a data interpolant in a recursive
    way.  While Lagrange interpolation request an a priori knowledge of the n
    order of interpolant, a way of reducing the computation needed to test
    which polynomial order fits better is done by computing the Neville's Table.
    Interpolation nodes are created in a similar way such as Newton's divided
    difference. As an initial aproximation, nodes equal the f(x) data and are
    slowly force to fit function behaviour by comparing the difference in first 
    x data element with the following element in a forward way. Interval is set
    dividing the first data with the following element, until is been completed
    x data reading. When tolerance is not met, new nodes must be include or if 
    so increase tolerance error.
    
    Inputs: domainpnt - list - Elements that compose data x-domain. 
            imagepnt - list - Elements that compose data y-domain.
            tol - float - Criteria to check whether or not data fits with tolerance
                   
    Output: intrpnt - list - Polynomial coefficients of n-th grade              
    
    Example code: domainpnt = [(x*(10-0)/5)+x**2 for x in range(6)];
                  imagepnt = [(x*(10-0)/5)*x-x for x in range(6)];
                  tol = 0.05;
                  intrpnt = nevilletable(domainpnt, imagepnt, tol);
                  
    Dependencies: None.
    
    Version: 1.2 for Python 3.4
    
    Definitions are taken from:
        Richard L. Burden, J. Douglas Faires. "Numerical Analysis" 9th ed.
        "Chapter 3 - Interpolation and Polynomial Approximation". 
        Cengage Learning. 2010. pp: 117 - 123.
        
    Author: J.J. Cadavid - SFTC - EAFIT University.
    Contact: jcadav22@eafit.edu.co
    
    Date: 28/12/2014.
"""

def nevilletable(domainpnt, imagepnt, tol):

# Input values verification
    dm_sze = len(domainpnt);
    if dm_sze != len(imagepnt):
        raise Exception("Not equal number of nodes and images");

# Initial assignation - float type   
    evlpnt = domainpnt[0];
    intrpnt = imagepnt;

# Main loop - Coefficient calculation
    for columns in range (1, dm_sze):
        for rows in range(dm_sze-columns):
            intrpnt[rows] = ((evlpnt - domainpnt[rows + columns])*intrpnt[rows] + \
            (domainpnt[rows] - evlpnt)*intrpnt[rows + 1])/ \
            (domainpnt[rows] - domainpnt[rows + columns]);
    if abs(intrpnt[rows]-intrpnt[rows-1]) > tol:
        raise Exception("Tolerance not met - Increase nodes for better precision");
    return(intrpnt);