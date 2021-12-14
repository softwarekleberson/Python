import random

numero = random.randint(0, 5)
escolha = int(input('seu chute :'))

if escolha == numero:
    print('parabens você acertou')

else:
    print('tente de novo')

