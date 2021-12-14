n = s = 0
while True:
    n = int(input('digite numero :'))
    if n == 999:
        break
    s += n
print(f'a soma vale {s}')