# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
    Description: class numecinteg is a small class type python program used as 
    a prototipe algorithm. It's actual function is to represent a polynomial from
    a set of coefficients. The second feature is finding it's roots by applying
    Horner's algorithm.
    
    Method Inputs: None - Input built-in function takes data from user
                   
    Method Outputs: Polinomial visualization
                    py,pz,b0 - automatic tuple - Provides information of roots.
    
    Example code: [];
                  
    Dependencies: None.
    
    Version: 0.8 for Python 3.4
    
    Definitions are taken from:
        Richard L. Burden, J. Douglas Faires. "Numerical Analysis" 9th ed.
        "Chapter 2 - Solutions of Equations in One Variable". 
        Cengage Learning. 2010. pp: 92 - 96.
        
    Author: J.J. Cadavid - SFTC - EAFIT University.
    Contact: jcadav22@eafit.edu.co
    
    Date: 24/12/2014.
"""

class polyroot():
    
    polynm = None;
    coeff_str = None;
    polynm_var = None;
    
    def __getinfo():
        coeff_str = input('Enter polynomial Coefficients\n');
        polynm_var = input('Enter polynomial Variable\n');
        return coeff_str,polynm_var;
        
    def __getpolynm(coeff_str,polynm_var):
        coeff_list = coeff_str.split(',');
        coeff_sze = len(coeff_list);
        polynm = '%s' % (coeff_list[coeff_sze-1]);
        for i in range(1,coeff_sze):
            if len(coeff_list[coeff_sze-(i+1)])==1:
                polynm = '%s*%s**%d' % (coeff_list[coeff_sze-(i+1)],polynm_var,i)+polynm;
            else:
                polynm = '%s*%s**%d' % (coeff_list[coeff_sze-(i+1)],polynm_var,i)+'+'+polynm;
        return(coeff_list);
        
    def horner(coeff_sze,coeff_list,init_aprx):
        py = float(coeff_list[0]);
        pz = py;
        for j in range(1,coeff_sze):
            list_num = int(coeff_list[j]);
            py = init_aprx * py + list_num;
            pz = init_aprx * pz + py
        b0 = init_aprx * py + float(coeff_list[0]);
        return py,pz,b0;