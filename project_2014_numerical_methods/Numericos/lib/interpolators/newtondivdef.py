# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
    Description: function newtondivdef computes a data interpolant in a recursive
    way. In a similar way like Neville Table, Newton Divided difference makes
    a similar approach to fit data by evaluating the function in a certain
    shifted subset in domain and compare it in the non shifted place - Forward
    y element respect actual position y element. In a certain way it might look
    like this approach is similar to the limit definition of first derivative.
    Coefficients are store in a similar 1-row way done in nevilletable. Tolerance
    criteria is placed here as well, increase the number of nodes for better 
    fitting or increace tolerance error.
    
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
        Cengage Learning. 2010. pp: 124 - 126.
        
    Author: J.J. Cadavid - SFTC - EAFIT University.
    Contact: jcadav22@eafit.edu.co
    
    Date: 25/12/2014.
"""

def newtondivdef(domainpnt, imagepnt, tol):
    
    dm_sze = len(domainpnt);
    if dm_sze != len(imagepnt):
        raise Exception("Not equal number of nodes and images");
    
    intrpnt = imagepnt;
    for columns in range (1, dm_sze):
        for rows in range(dm_sze-columns):
            intrpnt[rows] = (intrpnt[rows] - intrpnt[rows + columns])/ \
            (domainpnt[rows] - domainpnt[rows + columns]);
            
    if abs(intrpnt[rows]-intrpnt[rows-1]) > tol:
        raise Exception("Tolerance not met - Increase nodes for better precision");