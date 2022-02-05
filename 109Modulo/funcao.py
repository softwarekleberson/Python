def aumenta(valor = 0, taxa = 0, formato=False):
    res = valor + (valor * taxa / 100)
    return res if formato is False else moeda(res)



def diminui(valor = 0, taxa = 0, formato=False):
    res = valor + (valor * taxa / 100)
    return res if formato is False else moeda(res) 



def dobra(valor = 0, formato=False):
    res =  valor * 2
    return res if formato is False else moeda(res)



def metade(valor = 0, formato=False):
    res = valor / 2
    return res if formato is False else moeda(res)



def moeda(valor = 0, moeda = 'R$'):
    return f'{moeda} {valor:>.2f}'.replace('.', ',')