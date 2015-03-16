Capitulo 01: Búsqueda de raíces
===============================

Descripción del método:
-----------------------

En este módulo se aplican los métodos de búsqueda de la raíces de una función, lo cual vendría a ser la búsqueda de todo elemento x que pertenezca al 
dominio de la función y que dicha función  cumpla f(x) = 0.

Se pretende que el usuario aplique los métodos a la solución de problemas, para lograr una mejor compresión sobre la temática y se adquieran
Habilidades que faciliten el progreso hacia otros métodos de mayor complejidad.

Dentro del paquete rootFinders se encuentran los siguientes métodos para la búsqueda de raíces en una función:

	-Bisection Method
	-FixedPoint Method
	-Müller Method
	-PolyRoot Method
	-RegulaFalse Method
	-Secant Method

Sequencia de llamado:
---------------------

Cada método corresponde a un archivo de extensión .py, que en el paquete se pueden encontrar como:

.. note:: bisection.py, fixedpoint.py, muller.py, polyroot.py, regulafalsi.py, secant.py.

Para ejecutar éstas funciones desde cualquier terminal de Python 3.4, es necesario cargar en memoria el paquete, con la línea:

.. note:: from Numericos.lib.rootFinders import *

Éste comando cargará simultaneamente los seis métodos del paquete. Para ejecutar un cálculo, es necesario agregar 'rootFinders.(método)',
y sus respectivos argumentos. En el caso de bisección la sequencia sería:

.. note:: rootFinders.bisection(('6*x-6'),-5,6,200,0.005);

En el caso de cargar un único método, se utiliza el comando:

.. note:: from Numericos.lib.rootFinders import muller

De ésta manera solamente el método de Müller esta disponible para operar. Ésta forma simplifica la forma de llamado.