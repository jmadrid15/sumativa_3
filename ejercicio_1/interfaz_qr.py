import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from ejercicio_1.generador_qr import GeneradorQR


class InterfazQR:
    def __init__(self, ventana_principal, funcion_regresar):
        self.ventana = ventana_principal
        self.ventana.title("Generador de QR")
        self.ventana.geometry("420x380")
        self.ventana.resizable(False, False)

        self.regresar = funcion_regresar

        #Instanciamos la lógica que importamos
        self.logica_qr = GeneradorQR()

        #Dibuja los componentes en la ventana
        self.crear_componentes()

    def crear_componentes(self):
        # --- SECCIÓN 1: URL ---
        lbl_url = tk.Label(self.ventana, text="1. Introduce la URL o enlace:", font=("Arial", 10, "bold"))
        lbl_url.pack(pady=(15, 2))

        self.entrada_url = tk.Entry(self.ventana, width=45, font=("Arial", 10))
        self.entrada_url.insert(0, self.logica_qr.url_defecto)
        self.entrada_url.pack(pady=5)

        #Tamaño del QR
        lbl_tamano = tk.Label(self.ventana, text="2. Selecciona el tamaño:", font=("Arial", 10, "bold"))
        lbl_tamano.pack(pady=(10, 2))

        self.combo_tamano = ttk.Combobox(self.ventana, values=["Pequeño", "Mediano", "Grande"], state="readonly",
                                         width=20)
        self.combo_tamano.set("Mediano")
        self.combo_tamano.pack(pady=5)

        #Color del QE
        lbl_color = tk.Label(self.ventana, text="3. Selecciona el color del QR:", font=("Arial", 10, "bold"))
        lbl_color.pack(pady=(10, 2))

        self.combo_color = ttk.Combobox(self.ventana, values=["Negro", "Azul", "Rojo", "Verde"], state="readonly",
                                        width=20)
        self.combo_color.set("Negro")
        self.combo_color.pack(pady=5)

        #Botones
        btn_generar = tk.Button(self.ventana, text="Generar Código QR", command=self.procesar_boton, bg="#4CAF50",
                                fg="white", font=("Arial", 11, "bold"), padx=10, pady=5)
        btn_generar.pack(pady=20)

        tk.Button(self.ventana, text="⬅️ Regresar al Menú", command=self.regresar, bg="#607D8B", fg="white",
                  font=("Arial", 9, "bold")).pack(pady=10)

    def procesar_boton(self):
        #Pide los datos de la UI y delega la creación del QR al backend
        enlace = self.entrada_url.get().strip()

        if not enlace:
            messagebox.showwarning("Faltan datos", "Por favor, introduce una URL válida.")
            return

        try:
            archivo_final = self.logica_qr.crear_codigo_qr(
                url=enlace,
                tamano_texto=self.combo_tamano.get(),
                color_texto=self.combo_color.get()
            )
            messagebox.showinfo("¡Éxito!", f"Código QR generado como '{archivo_final}'")

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo generar el QR: {str(e)}")