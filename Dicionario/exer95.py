jogador = dict()
gols = list()
time = list()

while True:
    
    print('-=' * 30)
    jogador['nome'] = str(input('Nome jogador :'))
    jogos = int(input(f'quantos jogos fez o jogador {jogador["nome"]} : '))
    
    gols.clear()
    for c in range(0, jogos):
        gols.append(int(input(f'quantos gols fez na partida {c + 1} :')))
    
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    
    controle = str(input(' Quer continuar : [S | N] ')).upper().split()[0]
    while controle not in 'S N':
        controle = str(input(' Erro responda apenas [S | N] : ')).upper().split()[0]
    
    if controle in 'N':
        break


print('-' * 45)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print()

while True:
    busca = int(input('Mostrar dados de qual jogador ? (999 para parar) :'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro ! Não existe jogador com código {busca}')
    else:
        print('-*' * 40)
        print(f' Levantamento do jogador {time[busca]["nome"]}')
        print('-*' * 40)
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i} fez {g} gols')
        print()
    print()
print('<< VOLTE SEMPRE >>')
    
    
    
        
        


        