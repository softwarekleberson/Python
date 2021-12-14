salario = float(input('qual o seu salario : '))

if salario > 1250:
    correcao = (salario + (salario * (10 / 100)))

elif salario <= 1250:
    correcao = (salario + (salario * (15 / 100)))

print('salario corrigido : {}'.format(correcao))