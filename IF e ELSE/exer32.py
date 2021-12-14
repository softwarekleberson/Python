ano = int(input('qual este ano : '))
dezena = ano // 1 % 10

if dezena % 4 == 0 and dezena > 0:
    print('ano bissesto')

else:
    print('ano não é bissesto')
