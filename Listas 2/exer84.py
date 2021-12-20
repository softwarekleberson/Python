temp = []
lista = []

maior = menor = 0

while True:
    
    temp.append(str(input('seu nome :')))
    temp.append(int(input('seu peso :')))   
    
    if len(lista) == 0:
        maior = menor = temp[1]
    
    else:
        if temp[1] > maior:
            maior = temp[1]
    
        elif temp[1] < menor:
            menor = temp[1]
         
    lista.append(temp[:])
    temp.clear()
    
    controle = str(input('quer continuar [S || N] :')).split()[0].upper()
    if controle in 'N':
        break
    
print('-=' * 30)
print(f'Ao todo cadastraram {len(lista)} pessoas ')
print(f'O maior peso foi de {maior} Kg. Peso de ', end=' ')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')

print()
print(f'O menor peso foi de {menor} Kg. Peso de ', end=' ')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')

