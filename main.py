import tkinter as tk
from ejercicio_1.interfaz_qr import InterfazQR
from ejercicio_2.interfaz_agenda import VistaAgenda
from ejercicio_3.interfaz_juego_colores import InterfazJuego
from ejercicio_4.interfaz_tareas import InterfazTareas


class MenúPrincipal:
    def __init__(self, ventana):
        self.ventana = ventana
        self.mostrar_menu_inicio()

    def limpiar_ventana(self):
        #Función hecha por la IA (no limpiaba la pantalla al ejecutar los ejercicios)
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def mostrar_menu_inicio(self):
        self.limpiar_ventana()

        self.ventana.title("Actividad Sumativa 3 - Menú")
        self.ventana.geometry("450x400")
        self.ventana.resizable(False, False)

        tk.Label(self.ventana, text="Menú - Ejercicios", font=("Arial", 14, "bold"), fg="#333").pack(pady=(20, 5))
        tk.Label(self.ventana, text="Seleccione el programa a ejecutar:", font=("Arial", 10, "italic"),
                 fg="gray").pack(pady=(0, 15))

        estilo_btn = {"font": ("Arial", 10, "bold"), "fg": "white", "width": 30, "pady": 6}

        tk.Button(self.ventana, text="1. Generador de Códigos QR", bg="#4CAF50", command=self.cargar_ejercicio_1,
                  **estilo_btn).pack(pady=6)
        tk.Button(self.ventana, text="2. Agenda de Contactos", bg="#4CAF50", command=self.cargar_ejercicio_2,
                  **estilo_btn).pack(pady=6)
        tk.Button(self.ventana, text="3. Juego Adivina el Color", bg="#4CAF50", command=self.cargar_ejercicio_3,
                  **estilo_btn).pack(pady=6)
        tk.Button(self.ventana, text="4. Gestor de Tareas Pendientes", bg="#4CAF50", command=self.cargar_ejercicio_4,
                  **estilo_btn).pack(pady=6)

        tk.Button(self.ventana, text="Salir del Programa", bg="#f44336", font=("Arial", 9, "bold"), width=15,
                  command=self.ventana.quit).pack(pady=25)

    # Carga de ejercicios, limpian primero y luego construyen el objeto
    def cargar_ejercicio_1(self):
        self.limpiar_ventana()
        InterfazQR(self.ventana, self.mostrar_menu_inicio)

    def cargar_ejercicio_2(self):
        self.limpiar_ventana()
        VistaAgenda(self.ventana, self.mostrar_menu_inicio)

    def cargar_ejercicio_3(self):
        self.limpiar_ventana()
        InterfazJuego(self.ventana, self.mostrar_menu_inicio)

    def cargar_ejercicio_4(self):
        self.limpiar_ventana()
        InterfazTareas(self.ventana, self.mostrar_menu_inicio)


if __name__ == "__main__":
    root = tk.Tk()
    app = MenúPrincipal(root)
    root.mainloop()
