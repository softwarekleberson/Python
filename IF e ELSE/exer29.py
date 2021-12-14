velocidade = float(input('digite sua velocidade :'))

if velocidade > 80:
    multa = ((velocidade - 80) * 7)
    print('Valor da multa : {}'.format(multa))

else:
    print('Abaixo da velocidade')