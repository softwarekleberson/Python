produtoPreco = (str(input('nome produto :')),
                float(input('preco prosuto :')),
                str(input('nome produto :')),
                float(input('preco produto :')),
                str(input('nome produto :')),
                float(input('digite preco produto :')))


print('TABELA DOS PRODUTOS E PRECOS \n')
print('************************************************ \n')

for nome, preco in enumerate(produtoPreco):
    if nome % 2 == 0:
        print(f'{produtoPreco[nome]}', end= ' ............ : ')
        
    else:
        print(f'{produtoPreco[nome]}')

