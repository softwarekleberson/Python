dados = dict()
lista = list()

soma = media = 0
while True:
    
    dados.clear()
    
    dados['nome'] = str(input('digite seu nome :'))
    
    sexo = str(input('seu sexo [M || F] : ')).upper().split()[0]
    while sexo not in 'M F':
        sexo = str(input('Apenas [M || F] : ')).upper().split()[0]

    dados['sexo'] = sexo
    dados['idade'] = int(input('sua idade :'))
    soma += dados['idade']
    
    lista.append(dados.copy())
    
    print('-=' * 30)
    controle = str(input('quer continuar [S || N] :')).upper().split()[0]
    while controle not in 'N S':
        controle = str(input('quer continuar [S || N] :')).upper().split()[0]

    if controle == 'N':
        break

print('-=' * 30)
print(f'Ao todo forão cadastradas : {len(lista)} pessoas')

media = soma / len(lista)
print(f'A media de idade foi de : {media:5.2f}')

print(f'As mulheres cadastradas foram ',end='')
for m in lista:
    if m['sexo'] in 'F':
        print(f'{m["nome"]} ' , end='')
        
print()
print('Lista das pessoas que estão acima da media de idade : ')

for p in lista:
    if p['idade'] >= media:
        print(' ')
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
        
print(" - - - - - - FIM PROGRAMA - - - - - - - - - - - -")
            
        
        


        


