palavras = ('musica', 'livro', 'cebola', 'programacao','investimento')

for palavra in palavras:
    print(f'\n Na palavra {palavra.upper()} temos ', end=' ')
    for vogal in palavra:
        if vogal.lower() in 'aeiou':
            print(vogal, end= ' ')

