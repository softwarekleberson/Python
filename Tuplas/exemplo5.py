a = (2,4,7,8,10,6,20,)
b = (10,12,14,16,18,20)
c = a + b

print(c)
print(len(c))
print(f'quantas vezes aparece o numero 20 : {c.count(20)} vezes ')
print(f'em qual posição está o 12 na tupla : {c.index(12)}')
print(f'pegar elemento a partir de uma posição, suponha que eu queira o proximo elemento {c.index(20, 10)}')