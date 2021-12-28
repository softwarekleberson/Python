jogador = dict()
gols = list()

print('-=' * 30)
jogador['nome'] = str(input('digite seu nome :'))

jogos = int(input(f'quantos jogos o {jogador["nome"]} fez :'))
for c in range(0, jogos):
    gols.append(int(input(f'quantos gols na partida {c + 1} : ')))

jogador['gols'] = gols[:]
jogador['total'] = sum(gols)

print('-=' * 30)
print(jogador)

print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} - - - - - tem valor {v}')
print('-=' * 30)




