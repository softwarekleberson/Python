a = int(input('digite numero :' ))
b = int(input('digite numero :' ))
c = int(input('digite numero :' ))

if a > b and a > c:
    maior = a

if b > a and b > c:
    maior = b

if c > a and c > b:
    maior = c

if a < b and a < c:
    menor = a

if b < a and b < c:
    menor = b

if c < a and c < b:
    menor = c

print('Maior : {}, Menor : {}'.format(maior, menor))