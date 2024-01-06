import tkinter as tk
from PIL import ImageTk, Image
import registrocliente
import  mostrarclientes
import registroservicio
import mostrarregistros

def accion1():
    registrocliente.mostrar_ventana_registro_cliente()

def accion2():
    mostrarclientes.mostrar_clientes_registrados()

def accion3():
    registroservicio.mostrar_ventana_servicio()

def accion4():
    mostrarregistros.mostrar_datos()

def mostrar_menu_principal():
    root = tk.Toplevel()
    root.title("Menú Principal")
    root.geometry("600x500")
    root.resizable(False, False)  # Evita la maximización


    # Cargar la imagen de fondo
    background_image = Image.open("fondo2.png")
    background_photo = ImageTk.PhotoImage(background_image)

    # Crear un lienzo para la imagen de fondo
    background_label = tk.Label(root, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Colores pastel para las etiquetas
    pastel_blue = "#d5dfff"
    pastel_pink = "#ffffff"

    # Creación de los botones con el mismo tamaño
    button_width = 20
    button_height = 2

    button1 = tk.Button(root, text="Registro de clientes", command=accion1, width=button_width, height=button_height, bg=pastel_pink)
    button1.place(relx=0.7, rely=0.20, anchor="center")

    button2 = tk.Button(root, text="Clientes Registrados", command=accion2, width=button_width, height=button_height, bg=pastel_pink)
    button2.place(relx=0.7, rely=0.35, anchor="center")

    button3 = tk.Button(root, text="Registro de servicios", command=accion3, width=button_width, height=button_height, bg=pastel_pink)
    button3.place(relx=0.7, rely=0.50, anchor="center")

    button4 = tk.Button(root, text="Ventas registradas", command=accion4, width=button_width, height=button_height, bg=pastel_pink)
    button4.place(relx=0.7, rely=0.65, anchor="center")

    root.mainloop()
