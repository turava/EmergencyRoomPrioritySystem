import unittest
from emergency_pryority_system import Paciente, SalaEmergencias, logger

class TestSalaEmergencias(unittest.TestCase):

    def setUp(self):
        self.sala = SalaEmergencias()

    def test_agregar_paciente(self):
        paciente = Paciente("Juan", 5, 3)
        self.sala.agregar_paciente(paciente)
        self.assertEqual(len(self.sala.max_heap), 1)
        self.assertEqual(len(self.sala.min_heap), 1)
        self.assertIn(paciente, self.sala.max_heap.data)
        self.assertIn(paciente, self.sala.min_heap.data)

    def test_atender_paciente_max_urgencia(self):
        paciente1 = Paciente("María", 10, 1)
        paciente2 = Paciente("Luis", 5, 2)
        self.sala.agregar_paciente(paciente1)
        self.sala.agregar_paciente(paciente2)

        self.sala.atender_paciente()
        self.assertNotIn(paciente1, self.sala.max_heap.data)
        self.assertNotIn(paciente1, self.sala.min_heap.data)

    def test_atender_paciente_mas_espera(self):
        paciente1 = Paciente("Carlos", 4, 6)
        paciente2 = Paciente("Ana", 6, 4)
        self.sala.agregar_paciente(paciente1)
        self.sala.agregar_paciente(paciente2)

        self.sala.atender_paciente()
        self.assertNotIn(paciente1, self.sala.max_heap.data)
        self.assertNotIn(paciente1, self.sala.min_heap.data)

    def test_atender_paciente_urgencia(self):
        paciente1 = Paciente("Diego", 7, 3)
        paciente2 = Paciente("Laura", 6, 4)
        self.sala.agregar_paciente(paciente1)
        self.sala.agregar_paciente(paciente2)

        self.sala.atender_paciente()
        self.assertNotIn(paciente1, self.sala.max_heap.data)
        self.assertNotIn(paciente1, self.sala.min_heap.data)

    def test_mostrar_pacientes(self):
        paciente1 = Paciente("Pedro", 8, 2)
        paciente2 = Paciente("Sofía", 9, 1)
        self.sala.agregar_paciente(paciente1)
        self.sala.agregar_paciente(paciente2)

        with self.assertLogs(logger, level='INFO') as log:
            self.sala.mostrar_pacientes()

        self.assertIn("Por urgencia (Max Heap):", "".join(log.output))
        self.assertIn("Paciente(Pedro", "".join(log.output))
        self.assertIn("Paciente(Sofía", "".join(log.output))

if __name__ == "__main__":
    unittest.main()
