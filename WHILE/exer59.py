recebe = False
maior = 0

while recebe != True:

    n1 = int(input('digite numero :'))
    n2 = int(input('digite numero :'))

    print(' = = = = = = = = = = = = = = = = = = = = OPÇÃO = = = = = = = = = = = = = == = = =')
    controle = int(input('Operação soma : [1] multplicação : [2] maior : [3] novos numeros : [4] sair : [5] ')) 
    
    if controle == 1:
        soma = n1 + n2
        print('soma {}'.format(soma))
    
    elif controle == 2:
        multplicacao = n1 * n2
        print('multiplicação {}'.format(multplicacao))
    
    elif controle == 3:

        if n1 > n2:
            maior = n1
            print('Maior {}'.format(maior))

        if n1 < n2:
            maior = n2
            print('Maior {}'.format(maior))
    
    elif controle == 4:
         n1 = int(input('digite numero :'))
         n2 = int(input('digite numero :'))
    
    elif controle == 5:
        recebe = True


    