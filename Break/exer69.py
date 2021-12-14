from random import randint

venceu = 0

while True:

    pc = randint(1,10)
    chute = int(input('quantos dedos :'))

    parImpar = ' '
    while parImpar not in 'PI':
        parImpar = str(input('par ou impar [P][i] :')).upper().strip()[0]

    rodada = pc + chute
    print(rodada)

    res = ''
    if rodada % 2 == 0:
        res = 'P'
                
    elif rodada % 2 != 0:
        res = 'I'
                    

    if res == parImpar:
        print(f'voce venceu, total de dedos {rodada}')
        venceu += 1
                
    else:
        print(f'Voce perdeu, total de dedos {rodada}')
        print(f'Você venceu {venceu} jogos')
        break

print(f'-'*80)
print('FIM')




       





        
