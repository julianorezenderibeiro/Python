import unittest


def fizz_buzz(n: int):
    resultado = []
    for i in range(1, n + 1):
        fizz_buzz_ou_algarismo = ''
        if i % 2 == 0:
            fizz_buzz_ou_algarismo = 'fizz'
        if i % 5 == 0:
            fizz_buzz_ou_algarismo += 'buzz'

        if fizz_buzz_ou_algarismo == '':
            fizz_buzz_ou_algarismo = str(i)
        resultado.append(fizz_buzz_ou_algarismo)
    return resultado


class TesteFizzBuzz(unittest.TestCase):
    def test_com_10(self):
        entrada = 10
        resultado = fizz_buzz(entrada)
        esperado = [
            '1',
            'fizz',
            '3',
            'fizz',
            'buzz',
            'fizz',
            '7',
            'fizz',
            '9',
            'fizzbuzz'
        ]
        self.assertListEqual(esperado, resultado)
