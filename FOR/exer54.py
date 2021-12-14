from datetime import date

maiorIdade = 0
menorIdade = 0

ano = date.today().year
anoAtual = int(ano)

for c in range(1,7):
    idade = int(input('quando você nasceu :'))
    grupo = anoAtual - idade

    if grupo >= 18:
        maiorIdade += 1
    elif grupo < 18:
        menorIdade += 1

print('Maiores de idade  : {}, menor de idade {}'.format(maiorIdade, menorIdade))