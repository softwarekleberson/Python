def ajuda(msg):
    
    help(msg)
        

programa = ''    
while True:
    parametro = str(input('qual funcao ou biblioteca :'))
    if parametro.upper() == 'FIM':
        break
    
    else:
        ajuda(parametro)
 

   