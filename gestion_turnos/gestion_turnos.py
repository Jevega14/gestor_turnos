# gestion_turnos/gestion_turnos.py

from collections import deque
from .cliente import Cliente

class GestionTurnos:
    def __init__(self):
        self.cola_prioritario = deque()
        self.cola_buena_gente = deque()
        self.cola_cliente_normal = deque()

    def agregar_cliente(self, cliente):
        if cliente.categoria == "Prioritario":
            self.cola_prioritario.append(cliente)
        elif cliente.categoria == "Buena Gente":
            self.cola_buena_gente.append(cliente)
        elif cliente.categoria == "Cliente Normal":
            self.cola_cliente_normal.append(cliente)

    def llamar_turno(self):
        if self.cola_prioritario:
            return self.cola_prioritario.popleft()
        
        for _ in range(3):
            if self.cola_buena_gente:
                yield self.cola_buena_gente.popleft()
        
        for _ in range(2):
            if self.cola_cliente_normal:
                yield self.cola_cliente_normal.popleft()
    
    def mostrar_colas(self):
        print("Prioritarios:", [c.id for c in self.cola_prioritario])
        print("Buena Gente:", [c.id for c in self.cola_buena_gente])
        print("Clientes Normales:", [c.id for c in self.cola_cliente_normal])
