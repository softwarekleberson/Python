aluno = dict()

aluno['nome'] = str(input('Qual seu nome :'))
aluno['media'] = float(input('Media :'))

if aluno['media'] > 6:
    aluno['situacao'] = 'aprovado'
else:
    aluno['situacao'] = 'reprovado'
    
print('-=' * 30)
for k, v in aluno.items():
    print(f'O campo : {k} e igual a  = {v}.')
print()