# notas 100, 50, 10 e 1 

print('{:-^60}'.format('Banco do Povo'))

while True:
    sacar = int(input('qual valor deseja sacar :'))

    valorCem = sacar // 100
    trococem =  sacar % 100

    valorCinquenta = trococem // 50
    trocoCinquenta = trococem % 50

    valorDez = valorCinquenta // 10
    trocoDez = valorCinquenta % 10

    valorUm = valorDez // 1
    trocoUm = valorDez % 1
     
    if valorUm == 1:
        break

print('{:-^60}'.format('FIM DO PROGRAMA'))
print(f'Notas de R$ : 100 {valorCem}, R$ : 50 {valorCinquenta} R$ : 10 {valorDez} R$ : 1 {valorUm}' )
print('{:-^60}'.format('Volte Sempre'))

    