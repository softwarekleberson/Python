mediaIdade = 0
maior = 0
contadorMulher = 0
nomeHomem = ''

for c in range(1,5):
    print(' = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =  DADOS = = = = =  = = = =  = = = =  = = = = ')
    nome = input('digite seu nome : ').upper().strip()
    sexo = input('qual o seu sexo FEMININO [F], MASCULINO [M] : ').upper().strip()
    idade = int(input('qual a sua idade :'))

    mediaIdade += idade / 4

    if sexo == 'M':
        maior = idade
        nomeHomem = nome
     
        if idade > maior:
            maior = idade
            nomeHomem = nome

    if sexo == 'F' and 20 >= idade:
        contadorMulher = contadorMulher + 1

print(' A media de idade do grupo é {}'.format(mediaIdade))
print('O homem mais velho tem {} anos, seu nome {}'.format(maior, nomeHomem))
print(' Ao todo são {} mulheres com menos de 20 anos'.format(contadorMulher))




