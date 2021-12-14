from datetime import date

atual = date.today().year
nasc = int(input('anos de nascimento :'))
anoAtual = int(atual)

idade = anoAtual - nasc

if idade == 18:
    print('Aliste imediatamente')

elif idade > 18:
    saldo = idade - 18
    print('voce deveria ter se alistado a {}'.format(saldo))

elif idade < 18:
    saldo = 18 - idade
    print('VocÊ deverá se alistar em :{} anos'.format(saldo))
