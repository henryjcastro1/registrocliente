import tkinter as tk
from tkinter import ttk
import sqlite3

def limpiar_visualizacion(tree):
    # Eliminar todos los items del Treeview (tabla)
    for item in tree.get_children():
        tree.delete(item)

def generar_archivo():
    conexion = sqlite3.connect('servicios.db')
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM registros_servicios ORDER BY fecha")
    filas = cursor.fetchall()

    with open('informacion_registrada.txt', 'w') as archivo:
        archivo.write("N° serv., Lavado, Secado, Jabón, Soflan, Vanish, Desengrasante, Pepas, Clorox, Total, Fecha\n")
        for fila in filas:
            fila_str = ', '.join(str(valor) if valor else '' for valor in fila)
            archivo.write(f"{fila_str}\n")

    conexion.close()
    print("Archivo generado exitosamente.")

def mostrar_datos():
    conexion = sqlite3.connect('servicios.db')
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM registros_servicios")
    filas = cursor.fetchall()

    conexion.close()

    mostrarregistros = tk.Tk()
    mostrarregistros.title("Datos de registros de servicios")

    tree = ttk.Treeview(mostrarregistros)
    tree["columns"] = ("id", "opcion1", "opcion2", "opcion3", "opcion4", "opcion5", "opcion6", "opcion7", "opcion8", "total", "fecha")
    
    tree.heading("#0", text="ID")
    tree.column("#0", minwidth=0, width=50)
    tree.heading("id", text="N° serv.")
    tree.heading("opcion1", text="Lavado")
    tree.heading("opcion2", text="Secado")
    tree.heading("opcion3", text="Jabón")
    tree.heading("opcion4", text="Soflan")
    tree.heading("opcion5", text="Vanish")
    tree.heading("opcion6", text="Desengrasante")
    tree.heading("opcion7", text="Pepas")
    tree.heading("opcion8", text="Clorox")
    tree.heading("total", text="Total")
    tree.heading("fecha", text="Fecha")

    tree.column("id", width=50)
    for column in ("opcion1", "opcion2", "opcion3", "opcion4", "opcion5", "opcion6", "opcion7", "opcion8"):
        tree.column(column, width=100)
    tree.column("total", width=80)
    tree.column("fecha", width=120)

    total_suma = 0

    for fila in filas:
        total = fila[9]
        total_suma += int(total) if total else 0

        values = [str(value) if value is not None else "" for value in fila]
        values[9] = f"{int(total):,}" if total else ""
        tree.insert("", "end", values=values)

    tree.pack(expand=True, fill=tk.BOTH)

    label_suma = tk.Label(mostrarregistros, text=f"Suma Total: {total_suma:,}", font=("Arial", 12, "bold"))
    label_suma.pack(pady=10)

    btn_generar_archivo = tk.Button(mostrarregistros, text="Generar Archivo", command=generar_archivo)
    btn_generar_archivo.pack(pady=10)

    btn_limpiar = tk.Button(mostrarregistros, text="Limpiar", command=lambda: limpiar_visualizacion(tree))
    btn_limpiar.pack(pady=10)

    mostrarregistros.mainloop()

if __name__ == "__main__":
    mostrar_datos()
