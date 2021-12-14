num1 = int(input('digite numero :'))
num2 = int(input('digite segundo valor :'))

if num1 == num2:
    print('numero um  {} é igual ao segundo numero {} '.format(num1,num2))

elif num1 > num2:
    print('primeiro numero {} é maior que o segundo {} '.format(num1,num2))

else:
    print('segundo numero {} e maior que o primeiro numero {}'.format(num2, num1))