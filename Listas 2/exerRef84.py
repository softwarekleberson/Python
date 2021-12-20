lista = list()
temp = list()

maior = menor = 0

while True:
    
    temp.append(str(input('Seu nome :')))
    temp.append(int(input('digite seu peso :')))
    
    if len(lista) == 0:
        maior = menor = temp[1]
    
    else:
        if temp[1] > maior:
            maior = temp[1]
    
        if temp[1] < menor:
            menor = temp[1]
        
    lista.append(temp[:])
    temp.clear()
        
    controle = str(input('quer continuar :')).upper().split()[0]
    if controle in 'N':
        break
    
print(f'Quantidade de pessoas cadastradas {len(lista)}')
print('*='*30)
    
print(f'O mais pesado possui {maior} e a pessoa ', end=' ')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}',end=' ')
    
print()
    
print(f'O mais leve possui {menor} e a pessoa ', end=' ')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}',end=' ')
    
    
    