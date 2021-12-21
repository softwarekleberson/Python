trabalhador = dict()

trabalhador['nome'] = str(input('Nome :'))
trabalhador['nascimento'] = int(input('Ano de nascimento :'))
trabalhador['carteira'] = int(input('0 não tem carteira :'))

if trabalhador['carteira'] > 0:
    trabalhador['contratacao'] = int(input('Ano de contratacao :'))
    trabalhador['salario'] = float(input('Seu salario :'))
    trabalhador['aposentadoria'] = trabalhador['contratacao'] + 30
    
print('-=' * 30)
for k, v in trabalhador.items():
    print(f' {k} ......... {v}')