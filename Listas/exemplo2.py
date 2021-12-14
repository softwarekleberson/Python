numeros = [1,2,2,7,48,5,8]

#coloca em ordem numerica reversa
numeros.sort(reverse=True)
print(numeros)

#conta quantos elemento possui
print(f'essa lista possui {len(numeros)}')

#insere elemento a partir de uma posicao definida
numeros.insert(2,4000)
print(numeros)

#remover elemento, mesmo ele estando duplicado na lista
#ira retirar apenas um elemento
numeros.remove(2)
print(numeros)

if 7 in numeros:
    numeros.remove(7)
else:
    print('nao achei valor')

print(numeros)
