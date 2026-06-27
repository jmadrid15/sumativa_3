class Agenda:
    def __init__(self):
        #Base de datos temporal
        self.contactos = {
            "Angy Hidalgo": "04121234567",
            "Deyker Hernández": "04241231212"
        }

    def agregar(self, nombre, telefono):
        self.contactos[nombre] = telefono
        return True

    def buscar(self, nombre):
        return self.contactos.get(nombre)

    def obtener_todos(self):
        return self.contactos