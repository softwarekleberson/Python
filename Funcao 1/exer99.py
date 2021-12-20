def maior(* num):
    
    maior = 0
    for v, i in enumerate(num):
        if v == 0:
            maior = i
        
        else:
            if i > maior:
                maior = i
    
    print(maior)
    
maior(2,4,6,8)
maior(10,5,60,7,20)
maior(90,50,10,5,70,30)