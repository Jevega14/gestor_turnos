# tests/test_cliente.py

import unittest
from gestion_turnos.cliente import Cliente

class TestCliente(unittest.TestCase):
    def test_creacion_cliente(self):
        cliente = Cliente(1, "Prioritario")
        self.assertEqual(cliente.id, 1)
        self.assertEqual(cliente.categoria, "Prioritario")

if __name__ == "__main__":
    unittest.main()
