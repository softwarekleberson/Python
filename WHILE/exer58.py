import random
aleatorio = random.randint(1,10)

cont = 1

acertou = False
while acertou != True:
    chute = int(input('chute numero :'))
    if chute == aleatorio:
        acertou = True

    else:
        cont += 1
        acertou = False

print('chutes dados {}'.format(cont))