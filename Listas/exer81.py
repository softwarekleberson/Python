lista = list()
while True:
    lista.append(int(input('digite numero : ')))
    
    controle = str(input('quer continuar [S][N] :')).upper().split()[0]
    while controle not in 'N S':
        controle = str(input('quer continuar [S][N] :')).upper().split()[0]
    
    if controle == 'N':
        break

print('-='*30)

print(lista)
print(f'Tamanho da lista {len(lista)}')

if 5 in lista:
    print('Valor 5 faz parte da lista')

else:
    print('5 nao faz parte da lista')

lista.sort(reverse=True)
print(f'Lista em ordem decrescente {lista}')

print('-='*30)
