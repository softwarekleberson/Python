times = ('santos','flamengo', 'cuiaba', 'fortaleza', 'chape', 'athetico mineiro', 'america', 'internacional',
         'juventude', 'sport')

print(f'Os 5 primeiros times {times[:5]}')
print(f'os ultimos 5 times {times[-4:]}')
print(sorted(times))
print(f'posicao da chapecoence {times.index("chape") + 1}')
