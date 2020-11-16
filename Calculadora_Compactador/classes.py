# -*- coding: utf-8 -*-
import zipfile
import os.path
import re
import math
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.constants import BOTTOM, DISABLED, END, EXTENDED,\
    HORIZONTAL, NORMAL, RIGHT, X, Y
from typing import List
from threading import Thread


class Calculadora:
    def __init__(
        self,
        calculadora: tk.Tk,
        Label: tk.Label,
        display: tk.Entry,
        buttons: List[List[tk.Button]]
    ):
        self.calculadora = calculadora
        self.label = Label
        self.display = display
        self.buttons = buttons

    def start(self):
        self._config_buttons()
        self._config_display()
        self.calculadora.mainloop()

    def _config_buttons(self):
        buttons = self.buttons
        for row_values in buttons:
            for button in row_values:
                button_text = button['text']

                if button_text == 'C':
                    button.bind('<Button-1>', self.clear)
                    button.config(bg='#EA4335', fg='#fff')

                if button_text in '0123456789.+-/*()^':
                    button.bind('<Button-1>', self.add_text_to_display)

                if button_text in '=':
                    button.bind('<Button-1>', self.calcular)
                    button.config(bg='#4785F4', fg='#fff')

    def _config_display(self):
        self.display.bind('<Return>', self.calcular)
        self.display.bind('<KP_Enter>', self.calcular)

    def _fix_text(self, text):
        # Substitui tudo que não for 0123456789./*-+^ para nada
        text = re.sub(r'[^\d\.\/\*\-\+\^\(\)e]', r'', text, 0)
        # Substitui sinais repetidos para apenas um sinal
        text = re.sub(r'([\.\+\/\-\*\^])\1+', r'\1', text, 0)
        # Substitui () ou *() para nada
        text = re.sub(r'\*?\(\)', '', text)

        return text

    def clear(self, event=None):
        self.display.delete(0, 'end')

    def add_text_to_display(self, event=None):
        self.display.insert('end', event.widget['text'])

    def calcular(self, event=None):
        fixed_text = self._fix_text(self.display.get())
        equations = self._get_equations(fixed_text)

        try:
            if len(equations) == 1:
                result = eval(self._fix_text(equations[0]))
            else:
                result = eval(self._fix_text(equations[0]))
                for equations in equations[1:]:
                    result = math.pow(result, eval(self._fix_text(equations)))

            self.display.delete(0, 'end')
            self.display.insert('end', result)
            self.label.config(text=f'{fixed_text} = {result} ')

        except OverflowError:
            self.label.config(
                text='Não consegui realizar essa conta, desculpe-me!')
        except Exception:
            self.label.config(text='Conta inválida')

    def _get_equations(self, text):
        return re.split(r'\^', text, 0)


class Compactador:

    def compactar(self, lista_arquivos):

        arquivo_zip = zipfile.ZipFile("arquivo.zip", "w")

        for arquivo in lista_arquivos:

            if(os.path.isfile(arquivo) and os.path.exists(arquivo)):

                base = os.path.basename(arquivo)
                arquivo_zip.write(arquivo, base)
        arquivo_zip.close()


class Aplicacao:

    def __init__(self,
                 master
                 ):

        self.frame = tk.Frame(master)
        self.frame.pack()

        self.botao_adicionar = tk.Button(self.frame)
        self.botao_adicionar["text"] = "Adicionar"
        self.botao_adicionar["command"] = self.adicionar
        self.botao_adicionar["bd"] = 3
        self.botao_adicionar["font"] = ("Arial", 12)
        self.botao_adicionar.pack(pady=10, padx=30, side="left")

        self.botao_deletar = tk.Button(self.frame)
        self.botao_deletar["text"] = "Deletar"
        self.botao_deletar["command"] = self.deletar
        self.botao_deletar["bd"] = 3
        self.botao_deletar["font"] = ("Arial", 12)
        self.botao_deletar.pack(padx=30, side="right")

        self.frame2 = tk.Frame(master)
        self.frame2.pack()

        self.sby = tk.Scrollbar(self.frame2)
        self.sby.pack(side=RIGHT, fill=Y)

        self.sbx = tk.Scrollbar(self.frame2, orient=HORIZONTAL)
        self.sbx.pack(side=BOTTOM, fill=X)

        self.listbox = tk.Listbox(self.frame2, width=60,
                                  height=20, selectmode=EXTENDED)
        self.listbox.pack()

        self.listbox.config(yscrollcommand=self.sby.set)
        self.sby.config(command=self.listbox.yview)
        self.listbox.config(xscrollcommand=self.sbx.set)
        self.sbx.config(command=self.listbox.xview)

        self.frame3 = tk.Frame(master)
        self.frame3.pack()

        self.botao_compactar = tk.Button(self.frame3)
        self.botao_compactar["text"] = "Compactar"
        self.botao_compactar["command"] = self.compactar
        self.botao_compactar["bd"] = 3
        self.botao_compactar["font"] = ("Arial", 12)
        self.botao_compactar.pack(pady=10)

    def adicionar(self):
        self.nome_arquivo = askopenfilename()
        if self.nome_arquivo != "":
            self.listbox.insert(END, self.nome_arquivo)

    def deletar(self):

        items = self.listbox.curselection()
        if len(items) == 0:
            messagebox.showinfo("Compactador", "Selecione pelo menos um item")
        else:
            pos = 0
            for i in items:
                item_pos = int(i) - pos
                self.listbox.delete(item_pos, item_pos)
                pos = pos + 1

    def compactar(self):
        lista_arquivos = self.listbox.get(0, END)
        if len(lista_arquivos) == 0:
            messagebox.showinfo(
                "Compactador", "Adicione arquivos para serem compactados")
            return

        def executar():
            self.botao_compactar.configure(state=DISABLED)
            compactador = Compactador()
            compactador.compactar(lista_arquivos)
            self.botao_compactar.configure(state=NORMAL)
        t = Thread(target=executar)
        t.start()
