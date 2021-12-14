altura = float(input('qual a sua altura :'))
peso = float(input('qual o seu peso :'))

imc =  peso / (altura * altura)

if imc < 18.5:
    print('Abaixo do peso seu imc :{} '.format(imc))

elif imc >= 18.5 and imc <= 25:
    print('peso ideal seu imc {}'.format(imc))

elif imc >= 25 and imc <= 30:
    print('sobrepeso seu imc {}'.format(imc))

elif imc >= 30 and imc <= 40:
    print('obesidade seu imc {}'.format(imc))

elif imc > 40:
    print('obsidade morbida seu imc {}'.format(imc))
