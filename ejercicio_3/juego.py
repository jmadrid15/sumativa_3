import random


class JuegoColores:
    def __init__(self):
        self.colores = ["Rojo", "Amarillo", "Verde", "Azul"]

        # Diccionario para saber si un color es cálido (1) o frío (0)
        self.temperaturas = {
            "Rojo": 1,
            "Amarillo": 1,
            "Verde": 0,
            "Azul": 0
        }

        self.color_secreto = ""
        self.reiniciar_juego()

    def reiniciar_juego(self):
        #Selecciona un nuevo color aleatorio de la lista
        self.color_secreto = random.choice(self.colores)

    def comprobar_intento(self, color_usuario):
        #Compara el intento del usuario y retorna el resultado o una pista
        if color_usuario == self.color_secreto:
            return "¡CORRECTO!"

        #Si no acertó, calculamos la pista basándonos en la temperatura
        temp_secreta = self.temperaturas[self.color_secreto]
        temp_usuario = self.temperaturas[color_usuario]

        if temp_secreta > temp_usuario:
            return "Incorrecto. Pista: Intenta con un color más cálido"
        elif temp_secreta < temp_usuario:
            return "Incorrecto. Pista: Intenta con un color más frío"
        else:
            #Si están en el mismo rango de temperatura:
            return "Incorrecto. Pista: Tienen la misma temperatura, ¡sigue intentando!"