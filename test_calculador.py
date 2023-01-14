import unittest;
from calculador import suma;
from calculador import resta;
from calculador import multiplicacion;
from calculador import division;


class TestCalculador(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(8, 4), 12)
    def test_resta(self):
        self.assertEqual(resta(8, 4), 4)
    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(8, 4), 32)
    def test_division(self):
        self.assertEqual(division(8, 4), 2)

if __name__ == '__main__':
    unittest.main()