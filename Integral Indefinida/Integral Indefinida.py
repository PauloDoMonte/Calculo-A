from sympy import *

init_printing()

x = Symbol('x')

funcao = input("Função: ")
print("Integral indefinida da funcao:",integrate(funcao,x),"+ C")
