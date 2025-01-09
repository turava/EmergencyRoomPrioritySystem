import logging
import random

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Paciente:
    def __init__(self, nombre, nivel_urgencia, horas_espera):
        self.nombre = nombre
        self.nivel_urgencia = nivel_urgencia
        self.horas_espera = horas_espera

    def __repr__(self):
        return f"Paciente({self.nombre}, Urgencia: {self.nivel_urgencia}, Espera: {self.horas_espera}h)"

class Heap:
    def __init__(self, key=lambda x: x, min_heap=True):
        self.data = []
        self.key = key
        self.min_heap = min_heap

    def _compare(self, parent, child):
        if self.min_heap:
            return parent > child
        else:
            return parent < child

    def push(self, item):
        self.data.append(item)
        self._sift_up(len(self.data) - 1)

    def pop(self):
        if len(self.data) == 0:
            raise IndexError("pop from empty heap")
        if len(self.data) == 1:
            return self.data.pop()

        root = self.data[0]
        self.data[0] = self.data.pop()
        self._sift_down(0)
        return root

    def _sift_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self._compare(self.key(self.data[parent]), self.key(self.data[index])):
            self.data[parent], self.data[index] = self.data[index], self.data[parent]
            index = parent
            parent = (index - 1) // 2

    def _sift_down(self, index):
        child = 2 * index + 1
        while child < len(self.data):
            right = child + 1
            if right < len(self.data) and self._compare(self.key(self.data[child]), self.key(self.data[right])):
                child = right

            if not self._compare(self.key(self.data[index]), self.key(self.data[child])):
                break

            self.data[index], self.data[child] = self.data[child], self.data[index]
            index = child
            child = 2 * index + 1

    def __len__(self):
        return len(self.data)

class SalaEmergencias:
    def __init__(self):
        self.max_heap = Heap(key=lambda x: -x.nivel_urgencia, min_heap=False)  # Para gestionar urgencias
        self.min_heap = Heap(key=lambda x: x.horas_espera)  # Para gestionar tiempos de espera

    def agregar_paciente(self, paciente):
        self.max_heap.push(paciente)
        self.min_heap.push(paciente)

    def atender_paciente(self):
        if len(self.max_heap):
            # Revisar si hay pacientes con urgencia máxima (nivel 10)
            if self.max_heap.data[0].nivel_urgencia == 10:
                paciente = self.max_heap.pop()
                self._eliminar_paciente_min_heap(paciente)
                logger.info(f"Atendiendo al paciente con máxima urgencia: {paciente}")

            # Revisar si hay pacientes que han esperado más de 5 horas
            elif self.min_heap.data[0].horas_espera > 5:
                paciente = self.min_heap.pop()
                self._eliminar_paciente_max_heap(paciente)
                logger.info(f"Atendiendo al paciente que ha esperado más de 5 horas: {paciente}")

            # Atender al paciente con mayor urgencia
            else:
                paciente = self.max_heap.pop()
                self._eliminar_paciente_min_heap(paciente)
                logger.info(f"Atendiendo al paciente con mayor urgencia: {paciente}")
        else:
            logger.info("No hay pacientes en espera.")

    def _eliminar_paciente_min_heap(self, paciente):
        self.min_heap.data = [p for p in self.min_heap.data if p != paciente]
        self._rebuild_heap(self.min_heap)

    def _eliminar_paciente_max_heap(self, paciente):
        self.max_heap.data = [p for p in self.max_heap.data if p != paciente]
        self._rebuild_heap(self.max_heap)

    def _rebuild_heap(self, heap):
        heap.data = sorted(heap.data, key=heap.key, reverse=not heap.min_heap)
        for i in range(len(heap.data) // 2 - 1, -1, -1):
            heap._sift_down(i)

    def mostrar_pacientes(self):
        logger.info("\nPacientes en la sala de emergencias:")
        logger.info("Por urgencia (Max Heap): %s", self.max_heap.data)
        logger.info("Por tiempo de espera (Min Heap): %s", self.min_heap.data)

# Simulación
def generar_pacientes_aleatorios(cantidad):
    nombres = ["Juan", "María", "Carlos", "Ana", "Luis", "Elena", "Pedro", "Sofía", "Diego", "Laura"]
    pacientes = []
    for _ in range(cantidad):
        nombre = random.choice(nombres)
        nivel_urgencia = random.randint(1, 10)
        horas_espera = random.randint(0, 10)
        pacientes.append(Paciente(nombre, nivel_urgencia, horas_espera))
    return pacientes

def main():
    sala = SalaEmergencias()
    pacientes = generar_pacientes_aleatorios(10)

    logger.info("\nAgregando pacientes a la sala de emergencias...")
    for paciente in pacientes:
        sala.agregar_paciente(paciente)
    
    sala.mostrar_pacientes()

    logger.info("\nSimulando atención de pacientes...")
    for _ in range(len(pacientes)):
        sala.atender_paciente()
        sala.mostrar_pacientes()

if __name__ == "__main__":
    main()
