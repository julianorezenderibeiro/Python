import tkinter as tk
from typing import List


def make_calculadora() -> tk.Tk:
    calculadora = tk.Tk()
    calculadora.title('Caculadora')
    calculadora.configure(padx=10, pady=10, background='#fff')
    calculadora.resizable(False, False)
    return calculadora


def make_label(calculadora) -> tk.Label:
    label = tk.Label(
        calculadora, text='Sem conta ainda',
        anchor='e', justify='right', background='#fff'
    )
    label.grid(row=0, column=0, columnspan=5, sticky='news')
    return label


def make_display(calculadora) -> tk.Entry:
    display = tk.Entry(calculadora)
    display.grid(row=1, column=0, columnspan=5, sticky='news', pady=(0, 10))
    display.config(
        font=('Helvetica', 40, 'bold'),
        justify='right', bd=1, relief='flat',
        highlightthickness=1, highlightcolor='#ccc'
    )
    display.bind('<Control-a>', display_control_a)
    return display


def display_control_a(event):
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')
    return 'break'


def make_buttons(calculadora) -> List[List[tk.Button]]:
    button_texts: List[List[str]] = [
        ['7', '8', '9', '+', 'C'],
        ['4', '5', '6', '-', '/'],
        ['1', '2', '3', '*', '^'],
        ['0', '.', '(', ')', '='],
    ]
    buttons: List[List[tk.Button]] = []

    for row, row_value in enumerate(button_texts, start=2):
        button_row = []
        for col_index, col_value in enumerate(row_value):
            btn = tk.Button(calculadora, text=col_value)
            btn.grid(row=row, column=col_index, sticky='news', padx=5, pady=5)
            btn.config(
                font=('Helvetica', 15, 'normal'),
                pady=40, width=1, background='#f1f2f3', bd=0,
                cursor='hand2', highlightthickness=0, highlightcolor='#ccc',
                activebackground='#ccc', highlightbackground='#ccc'
            )
            button_row.append(btn)
        buttons.append(button_row)
    return buttons
