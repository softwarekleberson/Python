def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gols')
    

nome = str(input('Qual seu nome : '))
gols = str(input('Quantos gols :'))

if gols.isnumeric():
    gols = int(gols)

else:
    gols = 0
    
if nome.strip() == '':
    ficha(gols=gols)

else:
    ficha(nome, gols)