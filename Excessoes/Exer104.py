from tkinter import N


def leiaInteiro(msg):
    
    while True:
        try:
            n = int(input(msg))
        
        except (ValueError, TypeError):
            print('digite valor inteiro  ')
            continue
        
        except(KeyboardInterrupt):
            print('usuario interrompeu o programa')
            return 0
        
        else:
            return n
        
        

def leiaReal(msg):
    
    while True:
        try:
            n = float(input(msg))
        
        except(ValueError, TypeError):
            print('digite valor real ')
            continue
        
        except(KeyboardInterrupt):
            print('usuario interrompeu o programa')
            return 0
        
        else:
            return n        



inteiro = leiaInteiro('digite seu inteiro : ')
real = leiaReal('digite seu real : ')

print(f'Inteiro {inteiro}, real {real}')