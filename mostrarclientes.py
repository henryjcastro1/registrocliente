import tkinter as tk
from tkinter import ttk
import sqlite3

def filtrar_clientes(entry, tree):
    texto_busqueda = entry.get()

    # Limpia el Treeview antes de cargar los resultados filtrados
    limpiar_treeview(tree)

    conexion = sqlite3.connect('clientes.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT rowid, nombre, apellido, documento, telefono, direccion, correo FROM clientes WHERE documento LIKE ?", ('%' + texto_busqueda + '%',))
    clientes_filtrados = cursor.fetchall()
    conexion.close()

    for cliente in clientes_filtrados:
        tree.insert("", tk.END, values=cliente)

def limpiar_treeview(tree):
    # Limpia todos los elementos del Treeview
    for i in tree.get_children():
        tree.delete(i)

def eliminar_cliente(tree, cliente_id):
    conexion = sqlite3.connect('clientes.db')
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM clientes WHERE rowid=?", (cliente_id,))
    conexion.commit()
    conexion.close()
    limpiar_treeview(tree)
    mostrar_clientes(tree)

def mostrar_clientes(tree):
    conexion = sqlite3.connect('clientes.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT rowid, nombre, apellido, documento, telefono, direccion, correo FROM clientes")
    clientes = cursor.fetchall()
    conexion.close()

    for cliente in clientes:
        tree.insert("", tk.END, values=cliente)

def mostrar_clientes_registrados():
    ventana_mostrar_clientes = tk.Tk()
    ventana_mostrar_clientes.title("Clientes Registrados")

    frame = tk.Frame(ventana_mostrar_clientes)
    frame.pack(fill=tk.BOTH, expand=True)

    tree = ttk.Treeview(frame, columns=("Nombre", "Apellido", "Documento", "Teléfono", "Dirección", "Correo"), show="headings")
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    tree.configure(yscrollcommand=scrollbar.set)

    tree.heading("Nombre", text="N° cliente")
    tree.heading("Apellido", text="Nombre")
    tree.heading("Documento", text="Apellido")
    tree.heading("Teléfono", text="Documento")
    tree.heading("Dirección", text="Teléfono")
    tree.heading("Correo", text="Dirección")

    mostrar_clientes(tree)

    entry_busqueda = tk.Entry(ventana_mostrar_clientes)
    entry_busqueda.pack(padx=10, pady=5)

    boton_buscar = tk.Button(ventana_mostrar_clientes, text="Buscar", command=lambda: filtrar_clientes(entry_busqueda, tree))
    boton_buscar.pack(padx=10, pady=5)

    menu = tk.Menu(ventana_mostrar_clientes, tearoff=0)
    menu.add_command(label="Eliminar cliente", command=lambda: eliminar_cliente(tree, tree.item(tree.selection())['values'][0]))

    def popup(event):
        if tree.selection():
            menu.post(event.x_root, event.y_root)

    tree.bind("<Button-3>", popup)

    ventana_mostrar_clientes.mainloop()