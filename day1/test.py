import unittest
from day1 import day_1
import os

#   Cuando el submarino cae por debajo de la superficie del océano, automáticamente realiza un barrido de sonar del fondo marino cercano.
#   En una pantalla pequeña, aparece el informe de barrido del sonar(su entrada del rompecabezas): cada línea es una medida de la profundidad del
#   fondo del mar a medida que el barrido se ve cada vez más lejos del submarino.
#
#   Por ejemplo, suponga que tiene el siguiente informe:
#
#   199
#   200
#   208
#   210
#   200
#   207
#   240
#   269
#   260
#   263
#   Este informe indica que, escanear hacia fuera desde el submarino, el sonar de barrido encontró profundidades de 199, 200, 208, 210, y así sucesivamente.
#
#   La primera orden del día es averiguar qué tan rápido aumenta la profundidad, solo para que sepa con qué está lidiando:
#    nunca se sabe si las llaves serán llevadas a aguas más profundas por una corriente oceánica o un pez o algo así.
#
#   Para hacer esto, cuente el número de veces que una medición de profundidad aumenta con respecto a la medición anterior.
#    (No hay ninguna medición antes de la primera medición). En el ejemplo anterior, los cambios son los siguientes:
#
#   199 (N/A - no previous measurement)
#   200 (increased)
#   208 (increased)
#   210 (increased)
#   200 (decreased)
#   207 (increased)
#   240 (increased)
#   269 (increased)
#   260 (decreased)
#   263 (increased)

#   En este ejemplo, hay 7 medidas que son más grandes que la medida anterior.
#
#   ¿Cuántas medidas son más grandes que la medida anterior?


class TestDia1(unittest.TestCase):

    def test_day_1_example(self):
        input = [
            199, 200, 208, 210, 200,
            207, 240, 269, 260, 263,
        ]
        self.assertEqual(day_1(input), 7)

    def test_day_3_example(self):
        input = [100, 101, 100, 199, 150,
                 200, 208, 210, 200, 150,
                 206, 208, 207, 212, 209,
                 200, 240, 269, 260, 263,
                 ]

        self.assertEqual(day_1(input), 11)
    
    def test_day_4_example(self):
        self.assertEqual(day_1(range(1, 100)), 98)


if __name__ == '__main__':
    unittest.main()
