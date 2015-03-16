# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
    Description: function hermitpoly calculates an interpolant based on Hermit
    interpolation aided with devided difference. Using the first derivative 
    along the domain.
    
    Inputs: domainlist - list object - list whose elements are x domain data.
            imagelist - list object - list whose elements are y domain data.
            derivalist - list object - list with first derivative data.
            
    Outputs: hermitcoeff - list object- Hermit interpolant coefficients.
    
    Example code: domainlist = [0 + (x*(10-0)/5)*x**2 for x in range(6)];
                  imagelist = [0 + (x*(10-0)/5)*x**4 for x in range(6)];
                  derivalist = [];
                  
    Dependencies: None.
    
    Version: 1.3 for Python 3.4
    
    Definition and structure were taken from:
        Richard L. Burden, J. Douglas Faires. "Numerical Analysis" 9th ed.
        "Chapter 3 - Interpolation and Polynomial Approximation". 
        Cengage Learning. 2010. pp: 133 - 141.
        
    Author: J.J. Cadavid - SFTC - EAFIT University.
    Contact: jcadav22@eafit.edu.co
    
    Date: 27/12/2014.
"""

def hermitpoly(domainlist, imagelist, derivalist):
    
    dm_sze = len(domainlist);    
    
    if dm_sze != len(imagelist) or dm_sze != len(derivalist):
        raise Exception( \
        "Not equal number of domain nodes, images or derivarive nodes");
    
    Z = [0]*(2*dm_sze + 1);
    hermitcoeff = [ [ 0 for i in range(2*dm_sze + 1) ] for j in range(2*dm_sze + 1) ];
         
    for i in range(dm_sze):
        Z[2*i] = domainlist[i];
        Z[2*i + 1] = domainlist[i];
        hermitcoeff[2*i][0] =  imagelist[i];
        hermitcoeff[2*i + 1][0] =  imagelist[i];
        hermitcoeff[2*i + 1][1] =  derivalist[i];
        
        if i != 0:
             hermitcoeff[2*i][1] = \
             (hermitcoeff[2*i][0] - hermitcoeff[2*i - 1][0])/(Z[2*i] - Z[2*i - 1]);
         
    for columns in range(2, (2*dm_sze + 1)):
        for rows in range(2, columns):
            hermitcoeff[columns][rows] = \
            (hermitcoeff[rows] - hermitcoeff[rows + columns])/ \
            (Z[rows] - Z[rows + columns]);
            
    return(hermitcoeff);