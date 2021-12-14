from datetime import date

atual = date.today().year
nasc = int(input('ano de nascimento :'))
anoAtual = int(atual)
idade = anoAtual - nasc

if idade <= 9:
    print('mirin')

elif idade <= 14:
    print('infantil')

elif idade <= 19:
    print('junior')

elif idade <= 20:
    print('senior')

else:
    print('master')