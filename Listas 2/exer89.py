auxiliar = list()
aluno = list()
media = 0
cont = 0

while True:
    
    cont += 1
    
    auxiliar.append(cont)
    auxiliar.append(str(input('seu nome : ')))
    auxiliar.append(float(input('sua nota 1 : ' )))
    auxiliar.append(float(input('sua nota 2 :' )))
    
    media = auxiliar[2] + auxiliar[3]
    media /= 2
    
    auxiliar.append(media)
    
    aluno.append(auxiliar[:])
    auxiliar.clear()
    
    controle = str(input('Quer Continuar [N || S] : ')).upper().split()[0]
    if controle in 'N':
        break


print('-=' * 30)
print('NO.   NOME             MÉDIA')
print('-=' * 30)

for i, descricao in enumerate(aluno):
    print(f'{descricao[0]}      {descricao[1]}', end= ' ')
    print(f'          {descricao[4]}') 
print('-=' * 30)


consulta = int(input('Quer a nota de qual aluno :'))
for i, descricao in enumerate(aluno):
    if consulta == descricao[0]:
        print(f'{descricao[1]}  ', end=' ')
        print(f'{descricao[2]} {descricao[3]}')
   


