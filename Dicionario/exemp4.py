pessoas = {'nome' : 'kleberson', 'sexo' : 'M', 'idade' : 23}
del pessoas['sexo']

pessoas['nome'] = 'Kobe'
pessoas['peso'] = 80.80 

for k, v in pessoas.items():
    print(f'{k} = {v}')