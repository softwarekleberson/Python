def leiaInt(msg):
    ok = False
    valor = 0
    
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
            
        else:
            print(f'Ero não e numero :')
        
        if ok:
            break
    
    return valor


n = leiaInt('digite numero :')
print(f'voce digitou o numero {n}')
        
    
    
    
    
    
    
    
    
    
    
    
    









