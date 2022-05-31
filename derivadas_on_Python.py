# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 19:30:45 2022

@author: andra
"""

# 30/032022 

# Calculando a derivada usando python (exercício da aula de Calculo I)
from sympy import *
import numpy as np

x, y, z = symbols('x y z')
init_printing(use_unicode = True)

diff(2*x**7 + cos(x),x) # ou f´(x) = 2*x^7 + cos(x)
# f´(x) = 14*x6 - sen(x)

diff(x+1/x*log(x),x) # log(x) = ln ("logaritmo natural" de x)

diff((x+1)/(x**2-1),x)


diff((x+1)/x*log(x),x)
diff((x**2+1)*exp(x))   # exp() é a mm coisa que "exponencial de x"

diff(5*x**3 + cos(x),x)

integrate(15*x**2 - sin(x),x) # seno é escrito como sin


diff(exp(x**2), x)


##=====================
import math

derivada1 = diff(0.0254*x**3 - 2.735*x**2 + 79.24*x - 176.25, x)
derivada2 = diff(0.0254*x**3 - 2.735*x**2 + 79.24*x - 176.25, x, x)
derivada3 = diff(0.0254*x**3 - 2.735*x**2 + 79.24*x - 176.25, x, x, x)

print(derivada1)
# 0.0762*x**2 - 5.47*x + 79.24

print(derivada2)
# 0.1524*x - 5.47

print(derivada3)
# 0.152400000000000

x = 20
num_novos_obitos = 0.0254*x**3 - 2.735*x**2 + 79.24*x - 176.25
print(f'O número de novos óbitos é', num_novos_obitos)

a = 0.0762
b = -5.47
c = 79.24
delta = b**2 - 4*a*c

x1 = (-b + math.sqrt(delta))//2*a
x2 = (-b - math.sqrt(delta))//2*a

print('A raiz x1 vale', x1)
print('A raiz x2 vale', x2)



