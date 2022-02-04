def votacao(nascimento):
    
    from datetime import date
    
    anoAtual = date.today().year
    idade = anoAtual - nascimento
    
    if(idade >= 18 and idade <= 65):
        return f"voce deve votar com :{idade}"
    
    elif(idade >= 16 and idade <= 17):
        return f"voto opcional com :{idade}"
    
    elif(idade > 65):
        return f"voto nao obrigatorio com :{idade}" 


nascimento = int(input('qual o ano do seu nascimento :'))
print(votacao(nascimento))

