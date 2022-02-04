from ast import Return
from operator import le


def notas(*n, show=False):
    valores = dict()
    
    valores['total'] = len(n)
    valores['maior'] = max(n)
    valores['menor'] = min(n)
    valores['media'] = sum(n) / len(n)
    
    if show:
        
        if valores['media'] >= 7:
            valores['situacao'] = 'Muito bom'
        
        if valores['media'] >= 5 and valores['media'] <= 6.9:
            valores['situacao'] = 'Razoavel'
        
        if valores['media'] < 5:
            valores['situacao'] = 'Ruim'
    
    return valores

resp = notas(2.4, 4.6, 1.2, 3.3, 5.0, 5.7, show=True)
print(resp)
    
