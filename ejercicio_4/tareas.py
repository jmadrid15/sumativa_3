class GestorTareas:
    def __init__(self):
        #Lista que guardará diccionarios. Ejemplo: {"texto": "Hacer tarea", "completada": False}
        self.lista_tareas = []
        self.archivo_datos = "tareas.txt"

        #Intentamos cargar tareas guardadas automaticamente al inicializar la clase
        self.cargar_desde_archivo()

    def agregar(self, texto_tarea):
        if texto_tarea:
            nueva_tarea = {"texto": texto_tarea, "completada": False}
            self.lista_tareas.append(nueva_tarea)
            return True
        return False

    def marcar_completada(self, indice):
        if 0 <= indice < len(self.lista_tareas):
            self.lista_tareas[indice]["completada"] = True
            return True
        return False

    def eliminar(self, indice):
        if 0 <= indice < len(self.lista_tareas):
            self.lista_tareas.pop(indice)
            return True
        return False

    def obtener_todas(self):
        return self.lista_tareas

    def guardar_en_archivo(self):
        #Guarda la lista de tareas en un archivo .txt
        try:
            with open(self.archivo_datos, "w", encoding="utf-8") as archivo:
                for tarea in self.lista_tareas:
                    # Traducimos el booleano a "1" (completada) o "0" (pendiente)
                    estado = "1" if tarea["completada"] else "0"
                    archivo.write(f"{estado}|{tarea['texto']}\n")
            return True
        except Exception:
            return False

    def cargar_desde_archivo(self):
        #Lee el archivo de texto. Si no existe, atrapa el error y arranca en blanco"""
        try:
            self.lista_tareas.clear()
            with open(self.archivo_datos, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea and "|" in linea:
                        estado_str, texto = linea.split("|", 1)
                        completada = True if estado_str == "1" else False
                        self.lista_tareas.append({"texto": texto, "completada": completada})
            return True
        except FileNotFoundError:
            return False
        except Exception:
            return False