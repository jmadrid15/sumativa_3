import tkinter as tk
from tkinter import messagebox
from ejercicio_2.agenda import Agenda


class VistaAgenda:
    def __init__(self, ventana, funcion_regresar):
        self.ventana = ventana
        self.ventana.title("Mis Contactos")
        self.ventana.geometry("400x500")
        self.ventana.resizable(False, False)

        self.regresar = funcion_regresar
        
        self.logica = Agenda()

        self.crear_componentes()

    def crear_componentes(self):
        #Entrada de datoss
        tk.Label(self.ventana, text="Nombre:", font=("Arial", 10, "bold")).pack(pady=(10, 2))
        self.entrada_nombre = tk.Entry(self.ventana, width=35, font=("Arial", 10))
        self.entrada_nombre.pack(pady=2)

        tk.Label(self.ventana, text="Teléfono:", font=("Arial", 10, "bold")).pack(pady=(10, 2))
        self.entrada_telefono = tk.Entry(self.ventana, width=35, font=("Arial", 10))
        self.entrada_telefono.pack(pady=2)

        #Botones
        btn_agregar = tk.Button(self.ventana, text="Agregar Contacto", command=self.procesar_agregar, bg="#4CAF50",
                                fg="white", font=("Arial", 9, "bold"), width=20)
        btn_agregar.pack(pady=5)

        btn_buscar = tk.Button(self.ventana, text="Buscar por Nombre", command=self.procesar_buscar, bg="#2196F3",
                               fg="white", font=("Arial", 9, "bold"), width=20)
        btn_buscar.pack(pady=5)

        btn_mostrar = tk.Button(self.ventana, text="Mostrar Todos", command=self.procesar_mostrar, bg="#FF9800",
                                fg="white", font=("Arial", 9, "bold"), width=20)
        btn_mostrar.pack(pady=5)

        #Resultados
        tk.Label(self.ventana, text="Lista de Contactos:", font=("Arial", 10, "bold")).pack(pady=(15, 2))
        self.caja_lista = tk.Text(self.ventana, width=45, height=10, font=("Arial", 10))
        self.caja_lista.pack(pady=5)

        tk.Button(self.ventana, text="⬅️ Regresar al Menú", command=self.regresar, bg="#607D8B", fg="white",
                  font=("Arial", 9, "bold")).pack(pady=10)

    #Acciones
    def procesar_agregar(self):
        nombre = self.entrada_nombre.get().strip()
        telefono = self.entrada_telefono.get().strip()

        if not nombre or not telefono:
            messagebox.showwarning("Atención", "Ambos campos son obligatorios.")
            return

        self.logica.agregar(nombre, telefono)
        messagebox.showinfo("¡Éxito!", f"'{nombre}' guardado correctamente.")

        self.entrada_nombre.delete(0, tk.END)
        self.entrada_telefono.delete(0, tk.END)
        self.procesar_mostrar()

    def procesar_buscar(self):
        nombre = self.entrada_nombre.get().strip()

        if not nombre:
            messagebox.showwarning("Atención", "Escribe el nombre a buscar.")
            return

        telefono_encontrado = self.logica.buscar(nombre)

        if telefono_encontrado:
            messagebox.showinfo("Encontrado", f"Nombre: {nombre}\nTeléfono: {telefono_encontrado}")
            self.entrada_telefono.delete(0, tk.END)
            self.entrada_telefono.insert(0, telefono_encontrado)
        else:
            messagebox.showerror("Error", f"'{nombre}' no existe en la agenda.")

    def procesar_mostrar(self):
        self.caja_lista.delete("1.0", tk.END)
        todos = self.logica.obtener_todos()

        if not todos:
            self.caja_lista.insert(tk.END, "La agenda está vacía.")
            return

        for nombre, telefono in todos.items():
            self.caja_lista.insert(tk.END, f" {nombre}  -->   {telefono}\n")