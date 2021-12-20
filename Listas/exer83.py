expr = str(input('digite sua expressao '))
pilha = []

for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print("expressao valida")
else:
    print('expressao invalida')


#
#expressao (a + b) / (c * b)
# 
# pilha = (
# pilha = pop (
#    
# Logo pilha = 0
# 
# pilha = (
# pilha = pop (
# 
# Logo pilha = 0
# 
#Logo len(pilha) == 0
# expressao valida
#

#
# Expressao invalida
# expressao(a + b) / c)
# 
# pilha = (
# pilha pop = )
# Logo pilha = 0
# 
#pilha == 0
# pilha.append(')')
# 
# logo pilha > 0
# 
# expressao invalida
# 
# 
# 
# 
# #


# 
# #




