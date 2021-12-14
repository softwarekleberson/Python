print('*'*30)
quantidade = int(input('quantos termos você quer :'))

t1 = 0
t2 = 1
print('{} -> {} ->'.format(t1, t2), end=' ')

cont = 3
while quantidade >= cont:
    
    t3 = t1 + t2
    print('{} -> '.format(t3), end=' ')

    t1 = t2
    t2 = t3

    cont += 1

print(' Fim')
print(' - '*30)