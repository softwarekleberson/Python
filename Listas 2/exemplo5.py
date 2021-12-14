galera = list()
dado = list()

for c in range(0, 3):
    dado.append(str(input('Nome : ')))
    dado.append(int(input('Idade : ')))
    galera.append(dado[:])
    dado.clear()

for i in galera:
    if i[1] > 18:
        print(f'{i[0]} maior de idade')
    
    else:
        print(f'{i[0]} menor de idade')
