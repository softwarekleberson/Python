def fatorial(n, show=False):
    
    """ 
    :return numero positivo
    :f referente a fatorial
    :show=True serve para mostrar o calculo sendo feito
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print(' X ', end=' ')
            else:
                print(' = ', end='')
        f *= c
    return f

#print(fatorial(5, show=True))
help(fatorial)