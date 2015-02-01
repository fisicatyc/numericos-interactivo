# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
    Description: function adapquad is an adaptive quadrature method based on 
    Simpson's rule for integration. It can also can be expanded into another 
    integration technique by replacing those lines. It provides more accurate 
    results by dividing the integration interval [a,b] into n subintervals, 
    and again applying integration rule until achiving desired tolerance in 
    each subinterval. If not met, the subinterval is divided again and the 
    process is done again.
    
    Inputs: lowerlimit - float or integer - integration interval element.
            upperlimit - float or integer - integration interval element.
            tol - float - desired error tolerance in calculated value.
            n - integer - numbers of levels or subintervals to generate.
            function - function type object - evaluates f(x) at x.
            
    Output: app - float - defined integral aproximation.
    
    Example line: adapquad(-2, 4, 0.005, 10, (lambda x: 4*sin(x)**2));
    
    Dependencies: None.
    
    Version: 1.1 for Python 3.4
    
    Definition and structure were taken from:
        Richard L. Burden, J. Douglas Faires. "Numerical Analysis" 9th ed.
        "Chapter 4 - Numerical differentiation and integration". 
        Cengage Learning. 2010. pp: 220 - 226.
        
    Author: J.J. Cadavid - SFTC - EAFIT University.
    Contact: jcadav22@eafit.edu.co
    
    Date: 29/12/2014.
"""

def adapquad (lowerlimit, upperlimit, tol, n, function):
    
# Initial input error verification
    test = lambda: None;
    if isinstance(function,type(test)) == 0:
        raise Exception("function must be lambda object-type");
        
# Zero initializing - list Type   
    tol = [0]*n;
    a = tol;
    h = tol;
    fa = tol;
    fc = tol;
    fb = tol;
    s = tol;
    l = tol;
    
# Initial value assignation - Definition of spatial grid size
    app = 0;
    i = 1;
    tol[i-1] = 10*tol;
    a[i-1] = lowerlimit;
    h[i-1] = (upperlimit - lowerlimit)/2;
    fa[i-1] = function(lowerlimit);
    fc[i-1] = function(lowerlimit + h);
    fb[i-1] = function(upperlimit);
    s[i-1] = h*(fa + 4*fc + fb)/3; # Simpson rule - can be change with other rule
    l[i-1] = 1;

# Main loop reasigns variables for each subinterval generated
    while i>0:
        fd = function(a[i-1] + h[i-1]/2);
        fe = function(a[i-1] + 3*h[i-1]/2);
        s1 = h*(fa[i-1] + 4*fd + fc[i-1])/6;
        s2 = h*(fc[i-1] + 4*fe + fb[i-1])/6;
        v1 = a[i-1];
        v2 = fa[i-1];
        v3 = fc[i-1];
        v4 = fb[i-1];
        v5 = h[i-1];
        v6 = tol[i-1];
        v7 = s[i-1];
        v8 = l[i-1];
        i = i - 1;
        
        if abs(s1 + s2 - v7) < v6:
            app = app + (s1 + s2);
        else:
            if v8 >= n:
                raise Exception('Maximum level exceeded.')
            else:
                i = i + 1;
                a[i-1] = v1 + v5;
                fa[i-1] = v3;
                fc[i-1] = fe;
                fb[i-1] = v4;
                h[i-1] = v5/2;
                tol[i-1] = v6/2;
                s[i-1] = s2;
                l[i-1] = v8 + 1;
                i = i + 1;
                a[i-1] = v1;
                fa[i-1] = v2;
                fc[i-1] = fd;
                fb[i-1] = v3;
                h[i-1] = h[i-2];
                tol[i-1] = tol[i-2];
                s[i-1] = s1;
                l[i-1] = [i-2];
                
    return(app);