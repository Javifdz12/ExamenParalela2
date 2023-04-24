import unittest

class CuentaBancaria:
    def __init__(self, saldo_inicial=100):
        self.saldo = saldo_inicial

    def ingresar_dinero(self, cantidad):
        self.saldo += cantidad

    def retirar_dinero(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Saldo insuficiente")

    def obtener_saldo(self):
        return self.saldo

class PruebaCuentaBancaria(unittest.TestCase):
    def test_ingreso_y_retiro_dinero(self):
        cuenta = CuentaBancaria()

        # 40 procesos que ingresan 100 euros
        for _ in range(40):
            cuenta.ingresar_dinero(100)

        # 20 procesos que ingresan 50 euros
        for _ in range(20):
            cuenta.ingresar_dinero(50)

        # 60 procesos que ingresan 20 euros
        for _ in range(60):
            cuenta.ingresar_dinero(20)

        # 40 procesos que retiran 100 euros
        for _ in range(40):
            cuenta.retirar_dinero(100)

        # 20 procesos que retiran 50 euros
        for _ in range(20):
            cuenta.retirar_dinero(50)

        # 60 procesos que retiran 20 euros
        for _ in range(60):
            cuenta.retirar_dinero(20)

        # Comprobar que el saldo final es 100 euros
        self.assertEqual(cuenta.obtener_saldo(), 100)

