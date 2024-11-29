"""
A. Theatre Square
time limit per test1 second
memory limit per test256 megabytes
Theatre Square in the capital city of Berland has a rectangular shape with the size n × m meters. On the occasion of the city's anniversary, a decision was taken to pave the Square with square granite flagstones. Each flagstone is of the size a × a.

What is the least number of flagstones needed to pave the Square? It's allowed to cover the surface larger than the Theatre Square, but the Square has to be covered. It's not allowed to break the flagstones. The sides of flagstones should be parallel to the sides of the Square.

Input
The input contains three positive integer numbers in the first line: n, m and a (1 ≤ n, m, a ≤ 109).

Output
Write the needed number of flagstones.

Examples
InputCopy
6 6 4
OutputCopy
4
"""


import math

# Entrada
n, m, a = map(int, input().split())  # n = largo, m = ancho, a = tamaño de las baldosas


baldosas_largo = math.ceil(n / a)
""" 
La función math.ceil(x) devuelve el entero más pequeño que es mayor o igual a x.
En otras palabras, redondea hacia arriba el valor de x al siguiente número entero, incluso si x ya es un entero.
"""

baldosas_ancho = math.ceil(m / a)

# Calcular el número total de baldosas
total_baldosas = baldosas_largo * baldosas_ancho

# Salida
print(total_baldosas)
