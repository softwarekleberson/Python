import math

co = float(input('digite o cateto oposto : '))
ca = float(input('digite o cateto adjacente : '))

h1 = math.hypot(co, ca)

print('a hipotenusa vale {} '.format(h1))