maior = 0
menor = 0

for c in range(1,7):
    peso = float(input('qual o seu peso : '.format(c)))

    if c == 1:

        maior = peso
        menor = peso
    
    else:

        if peso > maior:
            maior = peso

        if peso < menor:
            menor = peso

print('Maior peso : {}, menor peso {}'.format(maior, menor))