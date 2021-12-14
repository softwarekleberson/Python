numero = int(input('qual o numero :'))
escolha = input('Transforma em binario (1), hexadecimal (2), octal (3) :').upper().strip()

if escolha == 'BINARIO':
    trasformacao = bin(numero)

elif escolha == 'HEXADECIMAL':
    trasformacao = hex(numero)

else:
    trasformacao = oct(numero)

print('O numero {} em decimal vale {} na transformação '.format(numero, trasformacao))