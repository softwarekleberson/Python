totCadastrados = 0
homensCadastrados = 0
mulheresCadastradas = 0

while True:

    print('-'*60)
    print('Cadastar Uma Pessoa')
    print('-'*60)

    idade = int(input('digite sua idade : '))
    sexo = ' '

    while sexo not in 'MF':
        sexo = str(input('Sexo : [M/F] ')).strip().upper()[0]


    if idade > 18:
        totCadastrados += 1
    
    if sexo == 'M':
        homensCadastrados += 1

    if sexo == 'F' and idade < 20:
        mulheresCadastradas += 1

    
    continuar = ' '

    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S][N] :')).strip().upper()[0]
    
    if continuar == 'N':
        break

print('-'*60)
print('------------------------------ FIM PROGRAMA -------------------------------------------')


print(f'Total de pessoas com mais de 18 anos : {totCadastrados}')
print(f'Total de homens cadstrados : {mulheresCadastradas}')
print(f'E temos {mulheresCadastradas} mulher com menos de 20 anos')