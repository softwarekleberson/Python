numero = int(input('digite o seu numero : '))

print('analisando o numero')

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10


print('Unidades : {}, Dezenas {}, Centenas {}, milhares {}'.format(u,d,c,m))