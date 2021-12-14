menorPreco = 0
precoMaiorMil = 1000
total = maiorMil = cont = 0
nomeMenor = ' '

while True:
    nomeProduto = str(input('nome do produto :'))
    preco = float(input('Preço: R$ '))
    cont += 1

    total = total + preco

    if preco > precoMaiorMil:
        maiorMil += 1
    
    if cont == 1 or preco < menorPreco:
        menorPreco = preco
        nomeMenor = nomeProduto
             
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('quer continuar [S][N] :')).upper().strip()[0]

    if continuar in 'N':
        break

print('{:-^60}'.format('FIM DO PROGRAMA'))
print('-'*60)

print(f'Preço total {total:.2f} dos produtos')
print(f'Produto custando mais de R$ 1000 : {maiorMil}')
print(f'Menor preco {menorPreco} é o produto {nomeMenor}')

