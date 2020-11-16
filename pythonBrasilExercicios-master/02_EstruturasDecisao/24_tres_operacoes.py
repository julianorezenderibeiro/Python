valor = float(input('Informe um numero: '))

print('1 - Par ou Impar')
print('2 - Positivo ou Negativo')
print('3 - Inteiro ou Decimal')
opcao = input('Escolha uma opcao: ')

if (opcao == '1'):
    if (valor % 2 == 0):
        print('Valor é par')
    else:
        print('Valor é impar')
elif (opcao == '2'):
    if (valor < 0):
        print('Valor é negativo')
    elif (valor > 0):
        print('Valor é positivo')
    else:
        print('Valor é igual a zero')
elif (opcao == '3'):
    if (valor == int(valor)):
        print('Valor é inteiro')
    else:
        print('Valor é decimal')
else:
    print('Opcao Invalida')
