def leiaInt(msg):
    ok = False
    numero = 0
    
    while True:
        n= str(input(msg))
        if n.isnumeric():
            numero = int(n)
            ok = True
        
        else:
            print('não e numero ')
        
        if ok:
            break
        
    return numero


n = leiaInt('digite numero  :')
print(f'voce digitou o numero {n}')