lista = list()

for c in range(0,5):
    n = int(input('digite numero : '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('adicionado final lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'adicionado na posicao {pos} da lista')
                break
            pos += 1

print('-=' * 30)
print(f'Valores adionado em ordem {lista}')