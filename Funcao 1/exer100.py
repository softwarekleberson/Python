from random import randint

def sorteio(lista):
    for v in range(0,5):
        lista.append(randint(1, 10))
    print(f'Sorteio {lista}')


def somaPar(lista):
    soma = 0
    for c, v in enumerate(lista):
        if v % 2 == 0:
            soma += v
    print(f'soma pares {soma}')
    

lista = list()
sorteio(lista)
somaPar(lista)


