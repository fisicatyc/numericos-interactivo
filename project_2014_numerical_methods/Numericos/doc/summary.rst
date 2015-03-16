Project Summary

Chapter #1:
Busqueda de raices

En este modulo se aplican los métodos de busqueda de la raices de una función, lo cual vendria a ser la busqueda de todo elemento x que pertenezca 
al dominio de la función y que dicha función  cumpla f(x) = 0
Se pretende que el usuario aplique los métodos a la solución de problemas, para lograr una mejor compresión sobre la temática y se adquieran
habilidades que faciliten el progreso hacia otros métodos de mayor complejidad.

Se encuentran los siguientes métodos para la busquedad de raices en una función.

	-Bisection Method
	-FixedPoint Method
	-Muller Method
	-PolyRoot Method
	-RegulaFalse Method
	-Secant Method

Chaptert #2:
Interpoladores

Este modulo se encarga de la implementación de los metodos de interpolación, que se basa en la problemática de tener n+1 puntos secuenciales,
donde x0 < x1 < x2 < x3 < ... < xn, y a partir de estos puntos diferentes se va a definir una función polinica que pase por esos puntos. 
Basicamente se esta aproximando p(x)= y a una f(x)= y original, a la cual probablemente no se tiene acceso o conocimiento. Esto se hace con el fin 
de modelar el comportamiento de los puntos anteriores y obtener el "polinomio interpolante". 

Se encuentran los siguientes métodos interpoladores:

	-BezierCUrve Method
	-Clampspline Method
	-Derivpol Method
	-Hermitpoly Method
	-Nevilletable Method
	-Newtondivdef Method


Chaptert #3: 
Diferenciadores

En este modulo se aplican los métodos diferenciadores o tambien conocidos como diferencias finitas. Se van a categorizar como 
diferencias centradas y no centradas, donde la primera define un conjunto de métodos numericos 
basandose en diferencias finitas con paso centrado. Y en los métodos no centrados se define un conjunto de métodos numericos basandose
en diferencias finitas SIN paso centrado. 

Estas técnicas se emplean muy a menudo en análisis numérico, especialmente en ecuaciones numéricas ordinarias, ecuaciones en diferencias y ecuaciones
en derivadas parciales. Las aplicaciones habituales suelen ser en los campos de la computación, áreas de la ingeniría térmica o en la
mecánica de fluidos.

Se encuentran los siguientes métodos diferenciadores centrados:

	-QCDA or Fourth Centered Difference Aproximation, calculates the fourth
    	 derivative in the interval.
	-SCDA or Second Centered Difference Aproximation, calculates the second
     	 derivative in the interval.
	-TCDA or Third Centered Difference Aproximation, calculates the third
    	 derivative in the interval.
	-QCDA or Fourth Centered Difference Aproximation, calculates the fourth
    	 derivative in the interval.	
	
Se encuentran los siguientes métodos diferenciadores no centrados:

	-nfirstderv
	-nsecondderv
	-snfirstderv
	

Chaptert #4:
Integradores

En este modulo se encuentran los métodos integradores que aproximan la funcion f(x) que se va a integrar por medio de polinomios interpolantes 
de diferentes grados, donde los métodos varian según el número de puntos o intervalo que se utilice para dicha aproximación permitiendon calcular
integrales defindas.

Exiten varios métodos que permiten realizar el proceso de hallar una integral defina y se dividen eneste proyecto en las siguientes categorias:

	-ClosedNewtonCotes
		*Fournodescotes
		*simprule
		*tesimprule
		*trapzrule
	-CompositeRules
		*Compmidtrule
		*compsimrule
		*comptraprule
	-DoubleIntegral
		*Gaussblint
		*Simpbdlintg
	-OpenNewtonCotes
		*Midpointrule
		*Onenodeopn
		*Thrnodeopn
		*twonodeopn
	-Tripleintegral
		*Gausstpllint
	-Adapquad
	-Natspline	
	-Romberginted


Chaptert #5:
Extrapoladores.

Este módulo se encarga de los métodos de exapolación, son métodos cientifico lógicos, que se basan en suponer que el curso de los acontecimientos 
continuara, es decir, afirma que existen unos axiomas y que estos son extrapolables a una nueva situación. La base de la extrapolación son observaciones 
secuenciales realizados en periodos conocidos de tiempo, estas observaciones son luego registradas como variables cuantitativas, medidas con algún tipo de escala.

Se usan para buscar soluciones a problemas lógicos o enseñar la misma pedagogía, lo cual los convierte en una herramienta muy utilizada en el marco
profesional y de enseñanza, no son necesariamente exclusorios de los métodos de interpolación y tampoco se pueden considerar únicos.

Se cuenta con los siguientes métodos:

	-Richarexpol o Extrapolación de Richardson