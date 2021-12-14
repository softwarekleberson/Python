from random import randint

maior = menor = 0

a = randint(0,10)
b = randint(0,10)
c = randint(0,10)
d = randint(0,10)
e = randint(0,10)

aleatorio = (a,b,c,d,e)

print(f'NUMEROS SORTEADOS')

for  pos, c in enumerate(aleatorio):
    print(f'Posicao {pos} : {c}')
    
for index, valor in enumerate(aleatorio):
    if index == 0:
        maior = menor = valor

    elif valor > maior:
        maior = valor
        
    elif valor < menor:
        menor = valor

print(f'Manior valor {maior}')
print(f'Menor valor {menor}')