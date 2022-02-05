import funcao

valor = float(input('valor :'))
taxa = float(input('taxa :'))

correcao = funcao.aumenta(valor, taxa)
print(f'Valor corrigido {correcao}')

dobraValor = funcao.dobra(valor)
print(f'Valor dobrado {dobraValor}')