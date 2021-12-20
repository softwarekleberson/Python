from time import sleep

def contador(i, f, p):
    
    if p < 0:
        p = p * -1
    
    if p == 0:
        p += 1
    
    print('-=' * 30)
    print(f' Contagem inicio : {i}, fim : {f}, passo {p}')
    sleep(2.5)
    
    if f > i:
        for c in range(i, f + 1, p):
            print(f'{c} ', end='', flush=True)
            sleep(0.5) 
        print('FIM')

    else:
        for c in range(i, f - 1, - p):
            print(f'{c} ', end='', flush=True)
            sleep(0.5) 
        print('FIM')

contador(1, 10, 1)
contador(10, 0, 2)

print('-=' * 30)
print('Contagem personalizada ')
inicio = int(input('Inicio : '))
fim = int(input('Fim : '))
passo = int(input('Passo : '))
print('-=' * 30)

contador(inicio, fim, passo)
