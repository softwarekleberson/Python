controle = True
while controle == True:
    sexo = input('digite seu sexo [M][F] :').upper()
    if sexo in 'M,F':
        controle = False
    else:
        controle = True

print('fim')