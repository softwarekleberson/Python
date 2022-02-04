from Funcoes import Numeros

num = int(input('digite numero :'))

fat = Numeros.fatorial(num)
duplicaValor = Numeros.dobro(num)

print(f'fatorial de {num} e {fat}')
print(f'O dobro de {num} e {duplicaValor}')