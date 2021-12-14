n = int(input('digite numero :'))
c = n
fat = 1

print('Calculando {} ! fatorial '.format(c))
while n >= 1:
    fat = fat * n
    n = n -1
print('{}'.format(fat))
    