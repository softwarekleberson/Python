div = 0

num = int(input('digite numero :'))
for c in range(1, num + 1):
    if num % c == 0:
        div = div + 1
        print(c)

if div == 2:
    print('Primo')

elif div > 2:
    print('Não é primo')