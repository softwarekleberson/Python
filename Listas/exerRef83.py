expr = str(input('digite sua expressao : '))
lista = []

for simb in expr:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
    
if len(lista) == 0:
    print('expressao valida')
if len(lista) > 0:
    print('expressao invalida')

            