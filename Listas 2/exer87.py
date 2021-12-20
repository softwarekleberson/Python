matriz = [[0,0,0],[0,0,0],[0,0,0]]
par = 0
coluna = 0
maior = 0


for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f' digite na posicao [{l}, {c}] :'))

for l in range(0,3):
    for c in range(0,3):
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]

for l in range(0,3):
    coluna += matriz[l][2]
    
for l in range(0, 3):
    if l == matriz[1][c]:
        maior = matriz[l][c]
    else:
        if maior < matriz[l][c]:
            maior = matriz[l][c]
            
for l in range(0,3):
    for c in range(0,3):
        print(f' [{matriz[l][c]}]', end= ' ')
    print()

print('=-'*30)
print()

print(f'A soma dos pares : {par}')
print(f'Coluna 2 soma : {coluna}')
print(f'Maior elemento da linha 2 : {maior}')

print('=-'*30)
print()