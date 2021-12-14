import random


nome1 = input('seu nome :')
nome2 = input('seu nome :')
nome3 = input('seu nome :')
nome4 = input('seu nome :')

orderLista = [nome1, nome2, nome3, nome4]
random.shuffle(orderLista)

print('apresentacao do trabalho {} '.format(orderLista))