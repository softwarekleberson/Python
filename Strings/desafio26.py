frase = input('digite uma frase :').upper().strip()

print("na frase a apareceu : {}".format(frase.count('A')))
print("o primeiro a esta na posicao: {}".format(frase.find('A') + 1))
print("o ultimo a apareceu na posicao {}".format(frase.rfind('A') + 1))