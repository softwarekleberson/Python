valores = (int(input('digite valores : ')),
           int(input('digite valor : ')),
           int(input('digite valor : ')),
           int(input('digite valor : ')),
           int(input('digite valor : ')))

print(f'{valores}')
print(f'O valor 9 apareceu {valores.count(9)} vez')

if 3 in valores:
    print(f'O valor 3 apareceru na posicao {valores.index(3)}')
else:
    print('Valor tres nao existente')

print('Valores pares foram', end= ' ')
for par, numeros in enumerate(valores):
   if numeros % 2 == 0:
       print(f'{numeros}', end=' ')






    
