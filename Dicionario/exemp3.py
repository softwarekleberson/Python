pessoas = {'nome' : 'kleberson', 'sexo' : 'M', 'idade' : 23}
for k in pessoas.keys():
    print(k)
    
print('-=' * 30)

for v in pessoas.values():
    print(v)
    
print('-=' * 30)

for k, v in pessoas.items():
    print(f'{k}  =  {v}')