nota1 = float(input('digite nota 1: '))
nota2 = float(input('digite segunda nota :'))

media = (nota1 + nota2) / 2

if media >= 6:
    print('Aprovado media {}'.format(media))

elif media >= 4 and 5.9 >= media:
    print('Recuperação media : {}'.format(media))

else:
    print('Reprovado {}'.format(media))