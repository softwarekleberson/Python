from time import sleep

def contador(i, f, p):
    
    """[summary]
        variavel i : inicio da contagem, valor
        variavel f : final da contagem
        variavel p : passo, valor dos pulos por vez
        Retorno : sem retorno
        Criador : Kleberson dos santos silva
    """
    
    if f > i:
        for c in range(i, f + 1, p):
            print(f'{c} ', end='', flush=True)
            sleep(0.5) 
        print('FIM')

    else:
        for c in range(i, f - 1, - p):
            print(f'{c} ', end='', flush=True)
            sleep(0.5) 
        print('FIM')

contador(1, 10, 1)

#Chamei a funcao help e passei como argumento a variavel contador, que vai explicar as variaveis dessa funcao
help(contador)




