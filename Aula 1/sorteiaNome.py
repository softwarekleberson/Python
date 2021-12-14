import random

nome1 = input('seu nome :')
nome2 = input('seu nome :')
nome3 = input('seu nome :')
nome4 = input('seu nome :')

sorteio = [nome1, nome2, nome3, nome4]
escolhido = random.choice(sorteio)

print('escolhido {}'.format(escolhido))

