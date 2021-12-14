primeiro = int(input('primeiro termo :'))
r = int(input('razao :'))
decimo = primeiro + (10 - 1) * r
for c in range(primeiro, decimo, r):
    print('{}'.format(c))
print('acabou')