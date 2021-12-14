lista = list()
par = list()
impar = list()

while True:
    
    lista.append(int(input('digite valor :')))
    
    controle = str(input('quer continuar [S][N] : ')).upper().split()[0]
    
    while controle not in 'N S':
        controle = str(input('quer continuar [S][N] : ')).upper().split()[0]
    
    if controle in 'N':
        break

for v in lista:
        
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)

print(lista)
print(f'Pares {par}')
print(f'Impares {impar}')