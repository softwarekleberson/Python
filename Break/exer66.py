soma = cont = 0

while True:
    n = int(input('digite numero :'))

    if n == 999:
        break

    cont += 1
    soma += n

print(f'soma {soma}, forão digitados {cont} numeros')