while True:

    cont = 0
    tabuada = int(input('qual tabuada você quer ?'))

    if tabuada < 0:
        break

    while cont <= 10:
        
        res = tabuada * cont
        print(f'{tabuada} x {cont} = {res}')
        cont += 1
    
    

   

