lanche = ('pizza', 'lanche', 'suco', 'chiquete')

print(f'todos os lanches {lanche}')
print(f'apenas o lanche na posição 2 {lanche[2]}')
print(f'vai de traz pra frente {lanche[-4]} nesse caso, PIZZA')
print(f'vai de posição 1 até o 2 : {lanche[1:3]}')
print(f'vai da posição 1 até o fim {lanche[1:]}')
print(f'vai de 0 ate a posição 1 {lanche[:2]}')
print(f'vai da posição -3 até o fim {lanche[-3:]}')

for comida in lanche:
    print(f'Eu vou comer {comida}')