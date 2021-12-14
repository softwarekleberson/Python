valorCasa = float(input('qual o valor da casa :'))
salarioComprador = float(input('salario comprador :'))
anosPagar = float(input('quantidade de anos a serem pagos :'))

meses = (anosPagar * 12)
prestacao = (valorCasa / meses)
condicaoEmprestimo = (salarioComprador * (30  / 100))

if condicaoEmprestimo > prestacao:
    print('Valor a ser pago {} em tantos meses {}'.format(prestacao, meses))

else:
    print('Emprestimo negado')