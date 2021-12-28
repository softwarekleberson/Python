from datetime import datetime


def voto(nascimento):
    from datetime import date
    
    atual = date.today().year
    idade = atual - nascimento

    if idade <= 16:
        return f'Voce não pode votar com {idade}'
    
    elif 18 <= idade and idade <= 65:
        return f'Voce deve votar com {idade}'
    
    else:
        return f'Você não precisa votar {idade}'


nascimento = int(input('Ano nascimento : '))
print(voto(nascimento))