
p = int(input('primeiro termo :'))
r = int(input('digite a razão :'))
controle = int(input('quantos termos você quer ver :'))

while controle != 0:

    termo = p
    while controle > 0:
        controle -= 1
        print('{} ->'.format(termo), end=' ')
        termo += r
    controle = int(input('Quantos termos a mais quer ver :'))
    print('Fim')