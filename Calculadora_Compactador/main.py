# utf-8
'''
from tkinter import messagebox
import tkinter

# hide main window
root = tkinter.Tk()
root.withdraw()

# message box display
messagebox.showerror("Error", "Error message")
messagebox.showwarning("Warning", "Warning message")
messagebox.showinfo("Information", "Informative message")

import numpy as np


def f(x0, x1):
    ans = np.log(x0) + np.log(x1)
    return ans


xn = 10
x0 = np.linspace(0, 10, xn)
x1 = np.linspace(0, 10, xn)
y = np.zeros((len(x0), len(x1)))
for i in range(xn-1):
    for il in range(xn-1):
        y[il, 10] = f(x0[i], x1[il])

xx0, xx1 = np.meshgrid(x0, x1)
print(xx0, xx1)

i = 10
print(i)
count = 1
print(count)
while count < i:
    count = count + 1
    if count >= i:
        break
while count > 0:
    count = count + 1
print(count)

a = 1
b = 1
print('hello world')
print(a == b)

# ksdhkjfhdkjhfk
# skdjfjsdljf
import pygame  # importando biblioteca de games
pygame.init()  # inicializando biblioteca
# criar janeja do jogo
janeja = pygame.display.set_mode((800, 600))
pygame.display.set_caption("criando jogo com Python")
janela_aberta = True

while janela_aberta:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

pygame.quit()

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

app = QApplication(['APSDU - PROTHEUS'])
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
# layout.setContentsMargins(100, 100, 100, 100)
# window.setLayout(layout)
# window.setGeometry(-1, -1, -1, -1)
window.show()
app.exec_()


# UTF-8
# Juliano Rezende Ribeiro
# Benedic, Domine Deus, in hac societate quae facit.

import PySimpleGUI as sg
import math


class TelaLojaTintas:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text(
                'Qual o tamanho em metros quadrados da área a ser pintada :'), sg.Input(key='qtde')],
            [sg.Button('Calcular')],
            [sg.Output(size=(100, 10))]
        ]
        # Janela
        self.janela = sg.Window(
            'Programa Loja de Tintas - Exercícios - Dúvidas - Forum Python Pro').layout(layout)

    def Iniciar(self):
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela.Read()
            qtde = self.values['qtde']
            print(
                f'De acordo com a quantidade da área a ser pintada de : {qtde} metros qudrados')

            print()
            print(f'Considerando o valor de R$ 80,00 por cada lata de 18 Litros de tinta')
            print()
            print(f'Levando em conta que cada 1 litro, cobre 3 metros quadrados')
            print()
            print(
                f'Serão necessários {math.ceil(int(qtde)/int(54))} lata de 18 litros')
            print()
            print(
                f'No custo total de R$ {(math.ceil(int(qtde)/int(54)))*int(80)}')


app = TelaLojaTintas()
app.Iniciar()

# Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar 1-matutino ou 2-Vespertino ou 3- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

a = input(' Informe o turno que frequenta (1) manhâ, (2) tarde ou (3) noite: ')

if a == '1':
    print('Bom dia')
else:
    if a == '2':
        print('Boa tarde')
    else:
        if a == '3':
            print('Boa noite')
        else:
            print(' Valor inválido, refaça a operação')


acao = input(' Informe a letra que deseja descobrir :').lower()

if acao.isalpha() and acao in 'aeiou':
    print('É vogal')
elif acao.isalpha() and acao not in 'aeiou':
    print('É consoante')
else:
    print('só é permitido letras!!!')


a = input(' Informe o turno que frequenta (1) manhâ, (2) tarde ou (3) noite: ')

if a == '1':
    print('Bom dia')
elif a == '2':
    print('Boa tarde')
elif a == '3':
    print('Boa noite')
else:
    print(' Valor inválido, refaça a operação')



           #  print(f'Considerando o valor de R$ 80,00 por cada lata de 18 Litros de tinta')
           # print()
           # print(f'Levando em conta que cada 1 litro, cobre 3 metros quadrados')
           # print()
           # print(
           #     f'Serão necessários {math.ceil(int(qtde)/int(54))} lata de 18 litros')
           # print()
           # print(
           #     f'No custo total de R$ {(math.ceil(int(qtde)/int(54)))*int(80)}')




import PySimpleGUI as sg
import math


class TelaSolucaoChocolate:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text(
                'Qual a quantidade de barras de chocolates :'), sg.Input(key='qtde')],
            [sg.Button('Calcular')],
            [sg.Output(size=(100, 10))]
        ]
        # Janela
        self.janela = sg.Window(
            'Programa com Função recursiva - Com mentoria do meu filho Bruno - Exercícios - Dúvidas - Forum Python Pro').layout(layout)

    def Iniciar(self):
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela.Read()
            qtde = self.values['qtde']
            print(
                f'De acordo com a quantidade de barra de chocolate informada : {qtde} ')

            print('Venci' if chocolate(int(qtde)) else 'Perdi')


def chocolate(n):
    if n == 42:
        return True
    elif n < 42:
        return False
    elif n % 2 == 0:
        return chocolate(n // 2)
    elif (n % 3 == 0 or n % 4 == 0):
        return chocolate((n % 10) * ((n // 10) % 10))
    elif n % 5 == 0:
        return chocolate(42)
    else:
        return False


app = TelaSolucaoChocolate()
app.Iniciar()


estado = input(
    'Informe seu estado civil casado (C), solteiro(S), viúvo (V) ou disquitado (D):').lower()

while estado != 'c' and estado != 's' and estado != 'v' and estado != 'd':
    print('ERRO: Estado civil inválido, repita a operação')
    estado = input(
        'Informe seu estado civil casado (C), solteiro(S), viúvo (V) ou disquitado (D):').lower()
    if estado == 'c' and estado == 's' and estado == 'v' and estado == 'd':
        break
    else:
        continue
print('Estado civil validado')
print('\nObrigado')
'''


a = int(input())
b = int(input())
if a == 1 and b == 1:
    print(f'satifez as duas condições {a} e {b}')
else:
    if a != 1 and b == 1:
        print(f'não satifez a condição de a ou seja {a}')
        print(f'mas satifez a condição de b ou seja {b}')
    elif a == 1 and b != 1:
        print(f'satifez a condição de a ou seja {a}')
        print(f'mas não satifez a condição de b ou seja {b}')
