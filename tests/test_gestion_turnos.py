import unittest
from gestion_turnos.cliente import Cliente
from gestion_turnos.gestion_turnos import GestionTurnos

class TestGestionTurnos(unittest.TestCase):
    def setUp(self):
        self.gestion_turnos = GestionTurnos()

    def test_agregar_cliente(self):
        cliente = Cliente(1, "Prioritario")
        self.gestion_turnos.agregar_cliente(cliente)
        self.assertIn(cliente, self.gestion_turnos.cola_prioritario)

    def test_llamar_turno_prioritario(self):
        cliente1 = Cliente(1, "Prioritario")
        cliente2 = Cliente(2, "Prioritario")
        self.gestion_turnos.agregar_cliente(cliente1)
        self.gestion_turnos.agregar_cliente(cliente2)
        turno = next(self.gestion_turnos.llamar_turno())
        self.assertEqual(turno.id, 1)
        turno = next(self.gestion_turnos.llamar_turno())
        self.assertEqual(turno.id, 2)

if __name__ == "__main__":
    unittest.main()
