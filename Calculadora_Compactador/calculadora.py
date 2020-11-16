from funcoes import make_calculadora, make_display, make_label, \
    make_buttons
from classes import Calculadora


def main():
    calculadora = make_calculadora()
    display = make_display(calculadora)
    label = make_label(calculadora)
    buttons = make_buttons(calculadora)
    calculadora = Calculadora(calculadora, label, display, buttons)
    calculadora.start()


if __name__ == '__main__':
    main()
