maior = menor = 0
posMaior = 0
posMenor = 0

numeros = list()

for c in range(0,4):
    numeros.append(int(input('digite valores :')))

print(numeros)

for i, v in enumerate(numeros):
    if i == 0:
        maior = menor = v
        posMaior = i
        posMenor = i
        
    if v > maior:
        maior = v
        posMaior = i
        
    if v < menor:
        menor = v
        posMenor = i

print( f'Maior valor {maior} na posicao {posMaior}')
print(f'Menor valor {menor} na posicao {posMenor}')