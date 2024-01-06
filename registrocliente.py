import tkinter as tk
from tkinter import messagebox
import sqlite3
from PIL import ImageTk, Image

# Función para validar la entrada del teléfono (solo números)
def validar_telefono(new_value):
    return new_value.isdigit() or new_value == ""

def mostrar_ventana_registro_cliente():
    # Función para insertar un cliente en la base de datos
    def insertar_cliente(nombre, apellido, documento, telefono, direccion, correo):
        try:
            # Conexión a la base de datos
            conexion = sqlite3.connect('clientes.db')
            cursor = conexion.cursor()

            # Verificar si el número de documento ya existe en la base de datos
            cursor.execute("SELECT COUNT(*) FROM clientes WHERE documento = ?", (documento,))
            cantidad = cursor.fetchone()[0]
            if cantidad > 0:
                # Mostrar un mensaje de error si el número de documento ya existe
                messagebox.showerror("Error", "El número de documento ya existe.")
                return
            
            # Verificar la presencia de "@" en el campo de correo electrónico
            if "@" not in correo:
                messagebox.showerror("Error", "Correo electrónico inválido. Debe incluir '@'")
                return            
            
            # Insertar un nuevo cliente si el número de documento no existe
            cursor.execute("INSERT INTO clientes (nombre, apellido, documento, telefono, direccion, correo) VALUES (?, ?, ?, ?, ?, ?)",
                            (nombre, apellido, documento, telefono, direccion, correo))
            conexion.commit()
            conexion.close()
            # Mostrar un mensaje de éxito luego de registrar al cliente
            messagebox.showinfo("Registro exitoso", "Cliente registrado exitosamente")

            # Borrar los datos de los campos de entrada después del registro exitoso
            nombre_entry.delete(0, tk.END)
            apellido_entry.delete(0, tk.END)
            documento_entry.delete(0, tk.END)
            telefono_entry.delete(0, tk.END)
            direccion_entry.delete(0, tk.END)
            correo_entry.delete(0, tk.END)

        except sqlite3.Error as error:
            # Manejar errores en caso de problemas con la base de datos
            messagebox.showerror("Error", "Error al registrar el cliente")

    # Función para registrar un nuevo cliente
    def registrar(nombre, apellido, documento, telefono, direccion, correo):
        if not all((nombre, apellido, documento, telefono, direccion, correo)):
            # Mostrar un mensaje si hay campos vacíos en el registro
            messagebox.showerror("Campos vacíos", "Por favor complete todos los campos.")
            return
        insertar_cliente(nombre, apellido, documento, telefono, direccion, correo)  


    # Crear una nueva ventana para el registro de clientes
    ventana_registro_cliente = tk.Toplevel()
    ventana_registro_cliente.title("Registro de Cliente")
    ventana_registro_cliente.geometry("400x300")
    ventana_registro_cliente.resizable(False, False)  # Impide que la ventana pueda maximizarse o agrandarse

     # Cargar la imagen como fondo
    background_image = Image.open("fondo3.png")
    background_photo = ImageTk.PhotoImage(background_image)

    # Crear un lienzo para la imagen de fondo
    background_label = tk.Label(ventana_registro_cliente, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Colores pastel para las etiquetas
    pastel_blue = "#d8e9ea"
    pastel_pink = "#fbdbf8"

    # Etiquetas y campos de entrada para los detalles del cliente
    tk.Label(ventana_registro_cliente, bg=pastel_blue, text="Nombre:").place(x=50, y=50)
    nombre_entry = tk.Entry(ventana_registro_cliente, width=30)
    nombre_entry.place(x=150, y=50)

    tk.Label(ventana_registro_cliente, bg=pastel_blue, text="Apellido:").place(x=50, y=80)
    apellido_entry = tk.Entry(ventana_registro_cliente, width=30)
    apellido_entry.place(x=150, y=80)

    tk.Label(ventana_registro_cliente, bg=pastel_blue, text="Documento:").place(x=50, y=110)
    documento_entry = tk.Entry(ventana_registro_cliente, width=30)
    documento_entry.place(x=150, y=110)

    tk.Label(ventana_registro_cliente, bg=pastel_blue, text="Teléfono:").place(x=50, y=140)
    telefono_var = tk.StringVar()
    validar_telefono_cmd = ventana_registro_cliente.register(validar_telefono)
    telefono_entry = tk.Entry(ventana_registro_cliente, width=30, textvariable=telefono_var,
                              validate="key", validatecommand=(validar_telefono_cmd, '%P'))
    telefono_entry.place(x=150, y=140)

    tk.Label(ventana_registro_cliente, bg=pastel_blue, text="Dirección:").place(x=50, y=170)
    direccion_entry = tk.Entry(ventana_registro_cliente, width=30)
    direccion_entry.place(x=150, y=170)

    tk.Label(ventana_registro_cliente, bg=pastel_blue, text="Correo:").place(x=50, y=200)
    correo_entry = tk.Entry(ventana_registro_cliente, width=30)
    correo_entry.place(x=150, y=200)

    # Botón para registrar al cliente
    registrar_button = tk.Button(ventana_registro_cliente, bg=pastel_pink, text="Registrar", 
                                 command=lambda: registrar(nombre_entry.get(), apellido_entry.get(),
                                                         documento_entry.get(), telefono_entry.get(),
                                                         direccion_entry.get(), correo_entry.get()))
    registrar_button.place(x=170, y=230)

    # Iniciar el bucle principal de la ventana
    ventana_registro_cliente.mainloop()
