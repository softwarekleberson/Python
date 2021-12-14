import math

angulo = float(input('digite o angulo : '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))

print('seno : {:.2f}, cosseno :{:.2f} '.format(seno, cosseno))
