# Imprime os numeros um abaixo do outro
for i in range(1, 21):
    print(i)
print()
# Imprime os numeros um ao lado do outro
for i in range(1, 21):
    if i < 21:
        print(i, end="")
    else:
        print(i)
print()

# Outra forma de imprimir os numeros um ao lado do outro
nsequencia = ''
for i in range(1, 21):
    nsequencia += str(i)
print(nsequencia)
