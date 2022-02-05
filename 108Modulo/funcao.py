def aumenta(valor = 0, taxa = 0):
    return valor + (valor * taxa / 100)

def diminui(valor = 0, taxa = 0):
    return valor + (valor * taxa / 100)

def dobra(valor = 0):
    return valor * 2

def metade(valor = 0):
    return valor / 2

def moeda(valor = 0, moeda = 'R$'):
    return f'{moeda} {valor:>.2f}'.replace('.', ',')