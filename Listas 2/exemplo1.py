teste = list()
galera = list()

teste.append('gustavo')
teste.append(40)

#Atencao será necessario usar o galera.append(teste[:]) * 2 vezes senao havera perda de dados

galera.append(teste[:])
teste[0] = 'kleberson'
teste[1] = 27
galera.append(teste[:])

print(galera)