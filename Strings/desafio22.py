#crie um programa que leia o nome completo de uma pessoa e mostre:

#O nome com todos as letras maisculas
#O nome com todas minusculas
#quantas letras ao todo(sem considerar espaçõs)
#quantas letras tem o primeiro nome

#Resolução, da 3 fez uma contagem do nome completo, e depois subtraio cada espaco achado, que seriam 
#os espacos do nome

#Resolução do 4 o find achou a posição de algo em especifivo no caso o ' ' e a sua posição

nome = input("digite seu nome : ").strip()

print("nome com letras maisculas " + nome.upper())
print("nome com letras minusculas " + nome.lower())
print("quantas letras possuem o nome sem espaco {} ".format(len(nome) - nome.count( ' ')))
print("quantas letras tem o primeiro nome {} ".format(nome.find( ' ')))