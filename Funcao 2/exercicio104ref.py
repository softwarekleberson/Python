def verificador(msg):
    
    num = 0
    ok = False
    
    while True:
        n = str(input(msg))
        if n.isnumeric():
            num = int(n)
            ok = True
        
        else:
            print('Nao e numero !')
            
        if ok:
            break
        
    return num            

n = verificador('digite numero :')
print(f'voce digitou o numero : {n}')
        