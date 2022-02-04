from exer107 import moeda

grana = int(input('quant de dinheiro : '))

aumentar = moeda.aumenta(grana)
descontar = moeda.desconto(grana)

print(aumentar)
print(descontar)