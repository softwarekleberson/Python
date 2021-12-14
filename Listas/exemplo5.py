a = [1,2,3,4,5]
b = a
b[2] = 100

print('possuem uma ligacao o que acontece em um reflete em outro')
# O valor 100 vai para as duas listas, como uma copia 
print(f'Lista A : {a} ')
print(f'Lista B : {b}')

#sem a copia

print('sem a copia do elemento \n')
c = [10,20,30,40]
d = c[:]
d[2] = 1000

print(c)
print(d)