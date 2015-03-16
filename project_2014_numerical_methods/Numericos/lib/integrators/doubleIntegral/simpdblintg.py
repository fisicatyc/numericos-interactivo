# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
    Description: function simpdblintg obtains a defined double integral 
    aproximation using Simpson Integration Rule by reducing intervals into
    subintervals. Similar to Double Legendre-Gauss Quadrature, calculations are
    done from inside to outsie, using outside domain to calculate inside 
    integration domain. The sum process in this method takes the results in 
    three stages, the endpoints of the interval, and subinterval results, this
    last one is devided on even and odd intervals. The heavy process is done
    within the subintervals by continuously modifying space grid size and by
    applying Simpson Rule. There is no need for use roots or coeficients from
    Legendre Polynomials for approximation, making it a bit faster than the
    Gauss-Legendre Quadrature, yet presicion might decrease if compare with it.
    
    Inputs: x_limits - list object - list with x first integral limits
            y_limits - list object - list with y second integral limits or functions
            evalpnt - list object - point to evaluate the derivatives.
            m - integer - number of subintervals in y domain.
            n - integer - number of subintervals in x domain.
            function - function object type - a double variable lambda object.
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
        Cengage Learning. 2010. pp: 240 - 244.
        
    Author: J.J. Cadavid - SFTC - EAFIT University.
    Contact: jcadav22@eafit.edu.co
    
    Date: 29/12/2014.
"""

def simpdblintg(x_limits, y_limits, m, n, function, flag=0):
    
# Input Verification    
    test = lambda: None;
    if flag == 0:
        if len(x_limits) != 2 or len(y_limits) != 2:
            raise Exception('Limits must include 2 values');
    else:
        if isinstance(y_limits[0],type(test)) == 0 or \
            isinstance(y_limits[1],type(test)) == 0:
            raise Exception("y limits must be lambda object-type");
    
    if m % 2 != 0 or n % 2 != 0:
        raise Exception('m and n must be positive even integers');
    
    if isinstance(function,type(test)) == 0:
        raise Exception("function must be lambda object-type");
    
# Zero intializing and initial assignation   
    hx = (x_limits[1] - x_limits[0])/n;
    j1 = 0;
    j2 = 0;
    j3 = 0;
    k2 = 0;
    k3 = 0;

# Main loop for nested Simpson Integration Rule   
    for i in range(n):
        x = x_limits[0] + i*hx;
        if flag != 0:
            var_yu = y_limits[1](x);
            var_yl = y_limits[0](x);
            k1 = (function(x, var_yl) + function(x, var_yu));
        else:
            var_yu = y_limits[1];
            var_yl = y_limits[0];
            k1 = (function(x, var_yl) + function(x, var_yu));
            
        hy = (var_yu - var_yl)/m;
        for j in range(1,(m - 1)):
            y = var_yl + j*hy;
            Q = function(x,y);
            
            if j % 2 == 0:
                k2 = k2 + Q;
            else:
                k3 = k3 + Q;
        L = hy/3*(k1 + 2*k2 + 4*k3);
        
        if i == 0 or i == n:
            j1 = j1 + L;
        elif i % 2 == 0:
            j2 = j2 + L;
        else:
            j3 = j3 + L;
        
    J = hx/3*(j1 + 2*j2 + 4*j3);
    return(J);