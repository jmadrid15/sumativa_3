import tkinter as tk
from tkinter import messagebox
from ejercicio_4.tareas import GestorTareas


class InterfazTareas:
    def __init__(self, ventana, funcion_regresar):
        self.ventana = ventana
        self.ventana.title("Mis Tareas Pendientes")
        self.ventana.geometry("400x520")
        self.ventana.resizable(False, False)

        self.regresar = funcion_regresar

        self.logica = GestorTareas()

        self.crear_componentes()
        #Refresca la pantalla por si el archivo ya traía datos guardados
        self.actualizar_pantalla()

    def crear_componentes(self):
        #Nueva tarea
        tk.Label(self.ventana, text="Nueva Tarea:", font=("Arial", 10, "bold")).pack(pady=(15, 2))
        self.entrada_tarea = tk.Entry(self.ventana, width=35, font=("Arial", 10))
        self.entrada_tarea.pack(pady=5)

        btn_agregar = tk.Button(self.ventana, text="Agregar Tarea", command=self.procesar_agregar, bg="#4CAF50",
                                fg="white", font=("Arial", 9, "bold"), width=18)
        btn_agregar.pack(pady=5)

        #Lista de Tareas
        tk.Label(self.ventana, text="Lista de Tareas:", font=("Arial", 10, "bold")).pack(pady=(15, 2))

        self.caja_tareas = tk.Listbox(self.ventana, width=45, height=12, font=("Arial", 10), selectmode=tk.SINGLE)
        self.caja_tareas.pack(pady=5)

        #Botones de control
        marco_acciones = tk.Frame(self.ventana)
        marco_acciones.pack(pady=10)

        btn_completar = tk.Button(marco_acciones, text="Marcar Completada", command=self.procesar_completar,
                                  bg="#2196F3", fg="white", font=("Arial", 9, "bold"), width=16)
        btn_completar.pack(side=tk.LEFT, padx=5)

        btn_eliminar = tk.Button(marco_acciones, text="Eliminar Tarea", command=self.procesar_eliminar, bg="#F44336",
                                 fg="white", font=("Arial", 9, "bold"), width=16)
        btn_eliminar.pack(side=tk.LEFT, padx=5)

        # Boton de guardado
        btn_guardar = tk.Button(self.ventana, text="💾 Guardar en Archivo", command=self.procesar_guardar, bg="#FF9800",
                                fg="white", font=("Arial", 10, "bold"), width=32)
        btn_guardar.pack(pady=15)

        tk.Button(self.ventana, text="⬅️ Regresar al Menú", command=self.regresar, bg="#607D8B", fg="white",
                  font=("Arial", 9, "bold")).pack(pady=10)

    def actualizar_pantalla(self):
        #Limpia la lista y la vuelve a llenar con datos
        self.caja_tareas.delete(0, tk.END)

        for tarea in self.logica.obtener_todas():
            marca = "✅ " if tarea["completada"] else "🔲 "
            self.caja_tareas.insert(tk.END, f"{marca} {tarea['texto']}")

    def procesar_agregar(self):
        texto = self.entrada_tarea.get().strip()
        if not texto:
            messagebox.showwarning("Atención", "Escribe una descripción para la tarea.")
            return

        self.logica.agregar(texto)
        self.entrada_tarea.delete(0, tk.END)
        self.actualizar_pantalla()

    def procesar_completar(self):
        try:
            indice_seleccionado = self.caja_tareas.curselection()[0]
            self.logica.marcar_completada(indice_seleccionado)
            self.actualizar_pantalla()
        except IndexError:
            messagebox.showwarning("Atención", "Por favor, selecciona una tarea de la lista.")

    def procesar_eliminar(self):
        try:
            indice_seleccionado = self.caja_tareas.curselection()[0]
            self.logica.eliminar(indice_seleccionado)
            self.actualizar_pantalla()
        except IndexError:
            messagebox.showwarning("Atención", "Por favor, selecciona la tarea que deseas eliminar.")

    def procesar_guardar(self):
        exito = self.logica.guardar_en_archivo()
        if exito:
            messagebox.showinfo("Guardado", "Las tareas se guardaron correctamente en 'tareas.txt'.")
        else:
            messagebox.showerror("Error", "No se pudieron guardar las tareas.")