p1 = int(input('primeiro termo : '))
r = int(input('digite a razão  '))
termo = p1

print('-=' * 60)
print(' PA ')
n = 0
while n <= 10:
    print('{} -> '.format(termo), end=' ')
    termo += r
    n += 1
print('FIM')
    