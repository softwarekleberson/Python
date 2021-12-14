numeros = list()

while True :
    
    valor = int(input('digite valor : '))
    
    if valor in numeros:
        print('digite outro valor ')
    
    else:
        numeros.append(valor)
    
    controle = str(input('quer continuar [S][N] : ')).upper().strip()[0]
    while controle not in 'S N':
        controle = str(input('quer continuar [S][N] : ')).upper().strip()[0]
    
    if controle == 'N':
        break
    
print('-=' * 30)
print(f'Valores {numeros}')
print('-=' *30 )


