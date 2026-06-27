import tkinter as tk
from ejercicio_1.interfaz_qr import InterfazQR

if __name__ == "__main__":
    #Inicializamos el contenedor del Tkinter
    root = tk.Tk()

    #Carga la interfaz pasandole el contenedor
    app = InterfazQR(root)

    #Mantiene la aplicación abierta
    root.mainloop()