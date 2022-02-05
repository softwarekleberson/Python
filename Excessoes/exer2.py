try:
    a = int(input('digite :'))
    b = int(input('digite :'))
    r = a / b

except (ValueError, TypeError):
    print('Problema com o tipo de dado informado')

except ZeroDivisionError:
    print('Não é possivel dividir um numero por zero !')

except KeyboardInterrupt:
    print('usuario não informou o valor')

else:
    print(f'o resultado é {r:.2f}')

finally:
    print('Tudo certo')