nome = input('digite o seu nome : ').strip()
espaco = nome.split()
print('seu primeiro nome : {}'.format(espaco[0]))
print('seu ultimo nome : {}'.format(espaco[len(espaco)- 1]))