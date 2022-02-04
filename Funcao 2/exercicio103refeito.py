def ficha(nome='<indefinido>', gols=0):
    print(f' nome :{nome} fez tantos gols :{gols}')

nome = str(input('qual o seu nome :'))
gols = str(input('quantos gols fez :'))

if gols.isnumeric():
    gols = int(gols)

else:
    gols = 0

if nome.strip() == '':
    ficha(gols=gols)

else:
    ficha(nome, gols)
    
    