try:
    a = float(input('digite :'))
    b = float(input('digite :'))
    r = a /b

except Exception as erro:
    print(f' O problema encontrado foi {erro.__class__} ')

else:
    print(f'Resultado da divisao {r:.2f}')
    
finally:
    print('Ate mais tarde, volte sempre')