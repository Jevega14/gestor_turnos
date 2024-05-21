from gestion_turnos.cliente import Cliente
from gestion_turnos.gestion_turnos import GestionTurnos

if __name__ == "__main__":
    gestion_turnos = GestionTurnos()

    # Agregar clientes
    gestion_turnos.agregar_cliente(Cliente(1, "Prioritario"))
    gestion_turnos.agregar_cliente(Cliente(2, "Buena Gente"))
    gestion_turnos.agregar_cliente(Cliente(3, "Cliente Normal"))
    gestion_turnos.agregar_cliente(Cliente(4, "Buena Gente"))
    gestion_turnos.agregar_cliente(Cliente(5, "Prioritario"))
    gestion_turnos.agregar_cliente(Cliente(6, "Cliente Normal"))

    # Mostrar estado de las colas
    gestion_turnos.mostrar_colas()

    # Llamar turnos
    for turno in gestion_turnos.llamar_turno():
        print(f"Llamado cliente con ID: {turno.id}")

    # Mostrar estado de las colas después de llamar turnos
    gestion_turnos.mostrar_colas()
