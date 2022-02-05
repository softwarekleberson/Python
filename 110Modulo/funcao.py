def aumenta(valor = 0, taxa = 0, formato=False):
    res = valor + (valor * taxa / 100)
    return res if formato is False else moeda(res)



def diminui(valor = 0, taxa = 0, formato=False):
    res = valor - (valor * taxa / 100)
    return res if formato is False else moeda(res) 



def dobra(valor = 0, formato=False):
    res =  valor * 2
    return res if formato is False else moeda(res)



def metade(valor = 0, formato=False):
    res = valor / 2
    return res if formato is False else moeda(res)



def moeda(valor = 0, moeda = 'R$'):
    return f'{moeda} {valor:>.2f}'.replace('.', ',')



def resumo(valor = 0, taxaAumento = 10, taxaDiminuir = 5):
    
    print('-' * 30)
    print('Resumo Das Operacoes'.center(30))
    
    print(f'Almento do preco : \t {aumenta(valor, taxaAumento, True)}')
    print(f'Diminuicao do valor : \t {diminui(valor, taxaDiminuir, True)}')
    print(f'Dobro do valor : \t {dobra(valor, True)}')
    print(f'Metade do valor  : \t {metade(valor, True)}')
    
    print('-' * 30)
    