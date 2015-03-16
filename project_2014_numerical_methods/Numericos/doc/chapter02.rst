Capitulo 02: Interpoladores
===========================

Descripción del método:
-----------------------
Este módulo se encarga de la implementación de los métodos de interpolación, que se basa en la problemática de tener n+1 puntos secuenciales,
donde x0 < x1 < x2 < x3 < ... < xn, y a partir de estos puntos diferentes se va a definir una función polinómica que pase por esos puntos. 
Básicamente se está aproximando p(x)= y a una f(x)= y original, a la cual probablemente no se tiene acceso o conocimiento. Esto se hace con el fin 
de modelar el comportamiento de los puntos anteriores y obtener el "polinomio interpolante". 

Se encuentran los siguientes métodos interpoladores:

	-BezierCUrve Method
	-Clampspline Method
	-Derivpol Method
	-Hermitpoly Method
	-Nevilletable Method
	-Newtondivdef Method
	-Natspline Method