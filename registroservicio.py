import tkinter as tk
from tkcalendar import DateEntry
import sqlite3
from tkinter import messagebox
from PIL import ImageTk, Image

def buscar_cliente_por_documento(documento):
    conexion = sqlite3.connect('clientes.db')
    cursor = conexion.cursor()

    cursor.execute("SELECT nombre, documento FROM clientes WHERE documento=?", (documento,))
    cliente = cursor.fetchone()

    conexion.close()

    return cliente

def mostrar_ventana_servicio():
    ventana_servicio = tk.Toplevel()
    ventana_servicio.title("Registro de Servicio")
    ventana_servicio.geometry("400x550")
    ventana_servicio.resizable(False, False)  # Evita la maximización

    # Colores pastel para las etiquetas
    pastel_blue = "#d5dfff"
    pastel_pink = "#ffffff"

    # Cargar la imagen de fondo
    background_image = Image.open("fondo4.png")
    background_photo = ImageTk.PhotoImage(background_image)

    # Crear un lienzo para la imagen de fondo en la ventana_servicio
    background_label = tk.Label(ventana_servicio, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    label_resultado = tk.Label(ventana_servicio, text="", bg=pastel_blue)
    label_resultado.grid(row=11, columnspan=2, pady=10)

    def buscar():
        documento = entry_documento.get()
        cliente = buscar_cliente_por_documento(documento)
        if cliente:
            nombre, documento = cliente
            label_nombre = tk.Label(ventana_servicio, text=f"Nombre: {nombre}", bg=pastel_blue)
            label_nombre.grid(row=1, column=0, pady=5)

            label_documento = tk.Label(ventana_servicio, text=f"Documento: {documento}", bg=pastel_blue)
            label_documento.grid(row=1, column=1, pady=5)

            # Crear 8 Checkbuttons
            checkbuttons = []
            for i in range(8):
                check_var = tk.BooleanVar()
                checkbutton = tk.Checkbutton(ventana_servicio, text=f"Opción {i+1}", variable=check_var, bg=pastel_blue)
                checkbutton.grid(row=i+2, column=0, pady=5)
                checkbuttons.append(check_var)

            # Campo para ingresar el total
            label_total = tk.Label(ventana_servicio, text="Total:", bg=pastel_blue)
            label_total.grid(row=10, column=0, pady=5)
            entry_total = tk.Entry(ventana_servicio)
            entry_total.grid(row=10, column=1, pady=5)

            # Campo para seleccionar la fecha
            label_fecha = tk.Label(ventana_servicio, text="Fecha:", bg=pastel_blue)
            label_fecha.grid(row=11, column=0, pady=5)
            entry_fecha = DateEntry(ventana_servicio, width=12, background='darkblue', foreground='white', borderwidth=2)
            entry_fecha.grid(row=11, column=1, pady=5)

            def registrar():
                # Obtener el estado de los Checkbuttons
                opciones = [1 if var.get() else 0 for var in checkbuttons]

                total = entry_total.get()
                fecha = entry_fecha.get()

                # Validar si el total es un número válido y está en unidades de mil
                if total.isdigit() and int(total) % 1000 == 0:
                    # Conectar con la base de datos
                    conexion = sqlite3.connect('servicios.db')
                    cursor = conexion.cursor()

                    # Insertar los valores en la base de datos
                    cursor.execute("INSERT INTO registros_servicios (opcion1, opcion2, opcion3, opcion4, opcion5, opcion6, opcion7, opcion8, total, fecha) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                   (*opciones, total, fecha))

                    conexion.commit()
                    conexion.close()

                    messagebox.showinfo("Registro Exitoso", "Los datos han sido registrados exitosamente.")

                else:
                    messagebox.showwarning("Error en el total", "Por favor, ingrese un número válido en unidades de mil.")

            boton_registrar = tk.Button(ventana_servicio, text="Registrar", command=registrar)
            boton_registrar.grid(row=12, columnspan=2, pady=10)

                    # Limpiar los campos después del registro exitoso
            entry_total.delete(0, tk.END)
            for var in checkbuttons:
                    var.set(0)  # Restablecer los Checkbuttons a su estado inicial

        else:
            messagebox.showwarning("Cliente no encontrado", "Cliente no encontrado")

    label_documento = tk.Label(ventana_servicio, text="Ingrese el número de documento:", bg=pastel_blue)
    label_documento.grid(row=0, column=0, pady=10)
    entry_documento = tk.Entry(ventana_servicio)
    entry_documento.grid(row=0, column=1, pady=5)

    boton_buscar = tk.Button(ventana_servicio, text="Buscar", command=buscar, bg=pastel_pink)
    boton_buscar.grid(row=0, column=2, pady=5)

    ventana_servicio.mainloop()
