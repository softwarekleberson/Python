controle = True
maior = menor = 0
media = 0
cont = 0
soma = 0

while controle == True:

    num = int(input('digite numero :'))
    cont += 1
    soma = soma + num

    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num

    media = (soma / cont)

    continuar = input('quer continuar [S], [N] :').upper()

    if continuar == 'N':
        controle = False

print('Você digitou {} numeros, '.format(cont), end=' ')
print(' media : {}, maior : {}, menor : {}'.format(media, maior, menor))
