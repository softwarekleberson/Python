numeros = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze',
           'doze','treze','quatorze','quinze','dessezeis','dessezete', 'desoito','desenove','vinte')

numero = int(input('Numero entre 0 e 20 : '))

while numero < 0 or numero > 20:
    numero = int(input('Numero entre 0 e 20 : '))

print(f'Seu numero {numeros[numero]}')
    