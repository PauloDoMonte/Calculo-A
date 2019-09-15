from sympy import *

init_printing()

x = Symbol('x')

funcao = input("Função: ")
a = int(input("Limite inferior de integração: "))
b = int(input("Limite superior de integração: "))
print("Integral definida da funcao:",integrate(funcao,(x,a,b)))
      
