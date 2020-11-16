sexo = input('Informe seu sexo (M/F): ')
altura = float(input('Informe sua altura (em metros): '))
peso = float(input('Informe o seu peso (em kg): '))

if (sexo == 'M'):
    pesoIdeal = (72.7 * altura) - 58
else:
    pesoIdeal = (62.1 * altura) - 44.7

if (peso > (pesoIdeal)):
    print('Voce esta acima do seu peso ideal:', pesoIdeal)
elif (peso < pesoIdeal):
    print('Voce esta abaixo do seu peso ideal:', pesoIdeal)
else:
    print('Voce esta no seu peso ideal:', pesoIdeal)
