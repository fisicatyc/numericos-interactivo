# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
    Description: function gausstpllint obtains a defined triple integral 
    aproximation using a nested gaussian quarature. The strategy of calculation
    is using the Legendre polynomials roots and coeficients. So that high grade 
    polynomials can be evaluated with accuracy. Adventage of this is the no need
    of equally spaced elements in domain. The function allows that the limits of 
    second or third integral can be variable as a function of the independent 
    variable or can be defined values. The second strategy of calculation is 
    the continuous calculation of the second variable space grid. Since it can 
    change, new grid size is created for every y value and z value.
    
    Inputs: x_limits - list object - list with x first integral limits
            y_limits - list object - list with y second integral limits or functions
            z_limits - list object - list with z second integral limits or functions
            evalpnt - list object - point to evaluate the derivatives.
            m - integer - number of subintervals in y domain.
            n - integer - number of subintervals in x domain.
            p - integer - number of subintervals in x domain.
            function - function object type - a double variable lambda object.
            roots - nested list - list of n, m order roots of Legendre Polynomials.
            coefflist - nested list - list of n, m coefficients of L. Polynomials.
            flag - integer - 0: defined y limits, 1: variable y limits. Default 0.
            
    Outputs: J - float - double integration aproximation.
    
    Example code: x_limits = [0, 5];
                  y_limits = [0, 5];
                  m = 3;
                  n = 2;
                  function = lambda x,y: y*x*3 + y**2 - x;
                  roots = [];
                  coefflist = [];
                  
    Dependencies: None.
    
    Version: 1.3 for Python 3.4
    
    Definition and structure were taken from:
        Richard L. Burden, J. Douglas Faires. "Numerical Analysis" 9th ed.
        "Chapter 4 - Numerical Differentiation and Integration". 
        Cengage Learning. 2010. pp: 245 - 246.
        
    Author: J.J. Cadavid - SFTC - EAFIT University.
    Contact: jcadav22@eafit.edu.co
    
    Date: 29/12/2014.
"""

def gausstpllint (x_limits, y_limits, z_limits, m, n, p, \
                    function, roots, coefflist, flag=0):
                        
# Initial input error verification
    test = lambda: None;
    if flag == 0:
        if len(x_limits) != 2 or len(y_limits) != 2 or len(z_limits):
            raise Exception('Limits must include 2 values');
    else:
        if isinstance(y_limits[0],type(test)) == 0 or \
            isinstance(y_limits[1],type(test)) == 0:
            raise Exception("y limits must be lambda object-type");
            
        if isinstance(z_limits[0],type(test)) == 0 or \
            isinstance(z_limits[1],type(test)) == 0:
            raise Exception("z limits must be lambda object-type");
    
    if isinstance(function,type(test)) == 0:
        raise Exception('function must be lambda object-type');
        
    if len(roots) != len(coefflist):
        raise Exception('Not equal number of roots and coefficients');

# Grid size calculation & initializing 
    h1 = (x_limits[1] - x_limits[0])/2;
    h2 = (x_limits[1] + x_limits[0])/2;
    jx = 0;
    jy = 0;
    J = 0;

# Main loop - domain x y generation - sum from inner integral to outside integral
    for i in range(1, m):
        x = h1*roots[i][m] + h2;
        if flag != 0:
            d1 = y_limits[1](x);
            c1 = y_limits[0](x);
        else:
            d1 = y_limits[1];
            c1 = y_limits[0];
        k1 = (d1 - c1)/2;
        k2 = (d1 + c1)/2;
        
        for j in range(1, n):
            y = k1*roots[j][n] + k2;
            if flag != 0:
                d1 = z_limits[1](x)(y);
                c1 = z_limits[0](x)(y);
            else:
                b1 = y_limits[1];
                a1 = y_limits[0];
            l1 = (b1 - a1)/2;
            l2 = (b1 + a1)/2;
            
            for k in range(1, p):
                z = l1*roots[k][p] + l2;
                Q = function(x, y, z);
                jy = jy + coefflist[k][p]*Q;
            
            jx = jx*coefflist[j][n]*l1*jy;
            
        J = J + coefflist[i][m];
        
    J = J*h1;
    return(J);