import tkinter as tk
from tkinter import messagebox
from ejercicio_3.juego import JuegoColores


class InterfazJuego:
    def __init__(self, ventana, funcion_regresar):
        self.ventana = ventana
        self.ventana.title("Adivina el Color")
        self.ventana.geometry("400x350")
        self.ventana.resizable(False, False)

        self.regresar = funcion_regresar

        self.logica = JuegoColores()

        self.crear_componentes()

    def crear_componentes(self):
        #Label de instrucciones del juego
        tk.Label(self.ventana, text="He pensado un color secreto!", font=("Arial", 12, "bold")).pack(pady=15)
        tk.Label(self.ventana, text="Selecciona un color para adivinar:", font=("Arial", 10)).pack(pady=5)

        #Container para los botones de colores
        #Usamos un Frame para alinear los botones en fila
        marco_botones = tk.Frame(self.ventana)
        marco_botones.pack(pady=10)

        #Pasamos el color directamente al metodo usando una función lambda
        tk.Button(marco_botones, text="Rojo", bg="#FFCDD2", fg="#B71C1C", font=("Arial", 10, "bold"), width=8,
                  command=lambda: self.procesar_intento("Rojo")).pack(side=tk.LEFT, padx=5)

        tk.Button(marco_botones, text="Amarillo", bg="#FFF9C4", fg="#F57F17", font=("Arial", 10, "bold"), width=8,
                  command=lambda: self.procesar_intento("Amarillo")).pack(side=tk.LEFT, padx=5)

        tk.Button(marco_botones, text="Verde", bg="#C8E6C9", fg="#1B5E20", font=("Arial", 10, "bold"), width=8,
                  command=lambda: self.procesar_intento("Verde")).pack(side=tk.LEFT, padx=5)

        tk.Button(marco_botones, text="Azul", bg="#BBDEFB", fg="#0D47A1", font=("Arial", 10, "bold"), width=8,
                  command=lambda: self.procesar_intento("Azul")).pack(side=tk.LEFT, padx=5)

        #Pistas y Resultados
        tk.Label(self.ventana, text="Resultado / Pistas:", font=("Arial", 10, "bold")).pack(pady=(25, 2))

        #Esta etiqueta cambiará dinámicamente para mostrar las pistas
        self.lbl_pista = tk.Label(self.ventana, text="Ningún intento todavía.", font=("Arial", 11, "italic"), fg="gray")
        self.lbl_pista.pack(pady=10)

        #Botón de reinicio
        self.btn_reiniciar = tk.Button(self.ventana, text="Jugar de Nuevo", command=self.reiniciar, bg="#9E9E9E",
                                       fg="white", font=("Arial", 9, "bold"), state="disabled")
        self.btn_reiniciar.pack(pady=20)

        tk.Button(self.ventana, text="⬅️ Regresar al Menú", command=self.regresar, bg="#607D8B", fg="white",
                  font=("Arial", 9, "bold")).pack(pady=10)

    def procesar_intento(self, color_seleccionado):
        #Envía el color a la lógica y reacciona según la respuesta
        respuesta = self.logica.comprobar_intento(color_seleccionado)

        if respuesta == "¡CORRECTO!":
            self.lbl_pista.config(text="¡Felicidades! ¡Acertaste!", fg="#4CAF50", font=("Arial", 12, "bold"))
            messagebox.showinfo("¡Ganaste!", f"¡Excelente! El color secreto era el {color_seleccionado}.")
            self.btn_reiniciar.config(state="normal", bg="#2196F3")  # Activamos el botón de reiniciar
        else:
            #Si falló, mostramos la pista
            self.lbl_pista.config(text=respuesta, fg="#F44336", font=("Arial", 11, "bold"))

    def reiniciar(self):
        #Limpia la pantalla y muestra un nuevo color
        self.logica.reiniciar_juego()
        self.lbl_pista.config(text="Ningún intento todavía.", fg="gray", font=("Arial", 11, "italic"))
        self.btn_reiniciar.config(state="disabled", bg="#9E9E9E")