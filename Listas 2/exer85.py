par = []
impar = []
lista = []

for c in range(0,7):
    
    num = int(input('digite numero :'))
    if num % 2 == 0:
        par.append(num)
        par.sort()
    
    if num % 2 != 0:
        impar.append(num)
        impar.sort()
       
lista.append(par[:])
par.clear()

lista.append(impar[:])
impar.clear() 

print(f'Lista com os pares {lista[0]} ', end=' ')
print(f'Lista com os impares {lista[1]}', end= ' ')


    