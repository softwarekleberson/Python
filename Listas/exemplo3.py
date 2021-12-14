numeros = [1,2,7,48,5,8]

#excluir ultimo elemento da lista
numeros.pop()
print(numeros)

#excluir elemento da lista usando a posicao do elemnto
numeros.pop(3)
print(numeros)
    
for c, v in enumerate(numeros):
    print(f'\n chave {c} valor {v}')