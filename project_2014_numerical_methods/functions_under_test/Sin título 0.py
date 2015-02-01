# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 15:24:23 2014

@author: Usuario
"""
coeff_str = input('Enter polynomial Coefficients\n');
init_aprx = 3;

coeff_list = coeff_str.split(',');
coeff_sze = len(coeff_list);

py = float(coeff_list[0]);
pz = py;
for j in range(1,coeff_sze):
    list_num = int(coeff_list[j]);
    py = init_aprx * py + list_num;
    pz = init_aprx * pz + py
