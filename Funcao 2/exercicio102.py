def fatorial(n, show=False):
    
    """[summary]
        Variavel n, show=True e show=False
        calcula o fatorial de um numero

    Returns:
        [type]: [description]
        n = numero a ser fatorado
        show = True, mostra o fatorial sendo calculado
        show = False mostra apenas o resultado
        return resultado do fatorial
    """
    
    fat = 1
    for c in range(n, 0, -1):
        
        if show ==True:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ',end='')
        fat *= c
    
    return fat

print(fatorial(5,show=False))
help(fatorial)