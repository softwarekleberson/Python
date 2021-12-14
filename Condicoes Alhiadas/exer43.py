print(' = = = = = = = = = = = = = = = LOJA DO PREÇÕ BOM = = = = = = =  = = = = = = = = = = = = ')

precoNormal = float(input('qual o preço normal do produto :'))
print('á vista ou cheque [ 1 ], á vista no cartão [ 2 ], cartão 2 vezes [ 3 ], cartão 3 vezes [ 4 ] ')
condicao = int(input('opção : '))

print(' = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ')

if condicao == 1:
    pagar = precoNormal - ((precoNormal * (10 / 100)))
    print('Pagar {} com desconto de 10 %'.format(pagar))

elif condicao == 2:
    pagar = precoNormal -  ((precoNormal * (5 / 100)))
    print('Pagar {} com desconto de 5 %'.format(pagar))

elif condicao == 3:
    print('preco normal {}'.format(precoNormal))

elif condicao == 4:
    pagar = precoNormal + (precoNormal * (20 / 100))
    print('você irá pagar {} acrescimo de 20 %'.format(pagar))