
class Cliente:
    def __init__(self, id, categoria):
        self.id = id
        self.categoria = categoria

    def __repr__(self):
        return f"Cliente(id={self.id}, categoria={self.categoria})"
