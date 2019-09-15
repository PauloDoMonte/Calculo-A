from __future__ import division
from sympy import *

init_printing()
x,y = symbols('x y')

global funcao
f_ = sympify(input("Função: "))
x0 = int(input("Ponto do calculo da reta da tangente: "))
f = Lambda(x, f_)

equacao_da_reta = (diff(f(x),x).subs(x,x0))*(x-x0) + f(x0)
print("Equação da reta:",equacao_da_reta)
