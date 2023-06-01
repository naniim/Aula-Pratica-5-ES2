import unittest
from calculadora_coprimo import CalculadoraCoprimo

class TestCalculador(unittest.TestCase):
    def setUp(self):
        self.calculadora = CalculadoraCoprimo()
    def testMDC(self):
        self.assertEqual(self.calculadora.mdc(12,28),4)
    def testMDCdeZero(self):
        self.assertEqual(self.calculadora.mdc(0,12345),12345)
    def testCoprimosdeUm(self):
        self.assertEqual(self.calculadora.QuantosCoprimos(1),0)
    def testCoprimos(self):
        self.assertEqual(self.calculadora.QuantosCoprimos(10),4)
