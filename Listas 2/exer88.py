from random import randint
from time import sleep

sorteio = list()
megaSena = list()
jogos = 0

cont = int(input('Quantos jogos você quer : '))
while cont > 0:
    
    for v in range(0,7):
        
        numeros = randint(1,60)
        if numeros not in sorteio:
            sorteio.append(numeros)
        sorteio.sort()
    
    megaSena.append(sorteio[:])
    sorteio.clear()
    
    cont -= 1

print('-=' * 30)


for i, j in enumerate(megaSena):
    
    jogos += 1
    
    sleep(1.5)
    print(f' {jogos} º sorteio {j}')
    
print('-=' * 30)