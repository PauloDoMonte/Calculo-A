from decimal import Decimal
from sympy import *

# Intervalo para simular o n tendendo ao infinito
n = 1
t = 1
e_ = Decimal((1+(1/n))**n)

while (t < 9):
        print("Numero de euler com N =",n, ":" ,Decimal((1+(1/n))**n))
        n = n*100
        t = t + 1
