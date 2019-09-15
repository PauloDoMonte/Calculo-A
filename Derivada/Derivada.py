from __future__ import division
from sympy import *

init_printing()
x,y = symbols('x y')

funcao = input("Função: ")
ordem = int(input("Ordem da derivada: "))

print("Derivada de ordem",ordem,":",diff(funcao,x,ordem))
