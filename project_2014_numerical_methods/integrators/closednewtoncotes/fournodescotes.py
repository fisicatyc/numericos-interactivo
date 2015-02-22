# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
    Description: class numecinteg is a set of numerical techniques applied to
    Numerical Integration, based on the elemental Closed Newton-Cotes and
    Open Newton-Cotes Formulas. This set holds the fundamental technique for
    highter ones like Composite Numerical Integration and Adapatative Quadrature.
    So for that extent, small integration intervals are required to achive certain
    presicion. The methods described here works in a similar way by taking an
    integration interval and reduced it in equally spaced elements or more 
    subintervals and sum each of them. The success of this techniques is based
    on parameter h, which is the space grid size. Lower spacing will grand better
    presicion, also truncation and round-off error will increase by minor changes
    in h, every technique differs on how it's analitical error increases. 
    
    The program set allows to input interpolated data or an analytical expression
    as a lambda object. More restriction is applied to interpolated data, since
    not all orders can be integrated properly with every technique. For high 
    interval integration, comptechrule.py or adapquad.py set is recommended.
    
    Method Inputs: lowerlimit - float - First element in integration interval
                   upperlimit - float - Last element in integration interval
                   function - lambda object type - evaluates f(x) at x -- or
                            - list - coefficients of interpolated data
                   flag - integer - optional - defines 0: lambda type 1: list type
                   
    Method Output: integ - float - Integration aproximation             
    
    Example code: integ = newtoncotesf(0, 6, lambda x: 2*x, flag = 0);

                  
    Dependencies: None.
    
    Version: 1.2 for Python 3.4
    
    Definitions are taken from:
        Richard L. Burden, J. Douglas Faires. "Numerical Analysis" 9th ed.
        "Chapter 4 - Numerical Differentiation and Integration". 
        Cengage Learning. 2010. pp: 193 - 201.
        
    Author: J.J. Cadavid - SFTC - EAFIT University.
    Contact: jcadav22@eafit.edu.co
    
    Date: 28/12/2014.
"""

def fournodescotes(lowerlimit, upperlimit, function, flag = 0):
        
    if flag == 0:
        test = lambda: None;
        if isinstance(function,type(test)) == 0:
            raise Exception("function must be lambda object-type");
            
        h = (upperlimit - lowerlimit)/4;
        sclowerlimit = lowerlimit + h;
        scupperlimit = upperlimit - h;
        midlimit = (sclowerlimit + scupperlimit)/2;
        
        integ = 2*h/45*(7*function(lowerlimit) + 32*function(sclowerlimit) + \
                + 12*(function(midlimit)) + 32*function(scupperlimit) + \
                7*function(upperlimit));
    else:
        if len(function) > 6:
            raise Exception("Interpolated function must be of fifth order maximum");
            
        integ = 2*h/45*(7*function[0] + 32*function[1] + \
                + 12*(function[2]) + 32*function[3] + 7*function[4]);
    return (integ);