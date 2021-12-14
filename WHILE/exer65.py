parada = 0
soma = 0

while parada != 999:
    parada = int(input('digite numero : [999] parar : '))
    if parada != 999:
        soma += parada

print('Soma {}'.format(soma))