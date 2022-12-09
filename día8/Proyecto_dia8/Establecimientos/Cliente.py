class Cliente:
    def __init__(self, nombre,apellidos,turno):
        self.nombre = nombre
        self.apellido = apellidos
        self.turno = turno

    def __str__(self):
        return f"{self.nombre} {self.apellido} su turno es el: {self.turno}"


