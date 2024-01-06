import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
import menu

def verificar_credenciales():
    usuario = username_entry.get()
    contraseña = password_entry.get()

    # Conectar a la base de datos
    conexion = sqlite3.connect('usuarios.db')
    cursor = conexion.cursor()

    # Verificar las credenciales en la base de datos
    cursor.execute("SELECT * FROM usuarios WHERE usuario=? AND contraseña=?", (usuario, contraseña))
    usuario_encontrado = cursor.fetchone()

    conexion.close()

    if usuario_encontrado:
        root.withdraw()  # Oculta la ventana de inicio de sesión
        menu.mostrar_menu_principal()  # Muestra la ventana del menú principal
    else:
        messagebox.showerror("Error de inicio de sesión", "Usuario o contraseña incorrectos")

root = tk.Tk()
root.title("Inicio de sesión")
root.geometry("700x400")
root.resizable(False, False)  # Evita la maximización

# Cargar la imagen de fondo
background_image = Image.open("fondo.png")
background_photo = ImageTk.PhotoImage(background_image)

# Crear un lienzo para la imagen de fondo
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Colores pastel para las etiquetas
pastel_blue = "#d5dfff"
pastel_pink = "#ffffff"

username_label = tk.Label(root, text="Usuario:", bg=pastel_blue)
username_label.place(relx=0.6, rely=0.35, anchor="center")

username_entry = tk.Entry(root, bg="lightgray", fg="black")
username_entry.place(relx=0.75, rely=0.35, anchor="center")

password_label = tk.Label(root, text="Contraseña:", bg=pastel_blue)
password_label.place(relx=0.6, rely=0.45, anchor="center")

password_entry = tk.Entry(root, show="*", bg="lightgray", fg="black")
password_entry.place(relx=0.75, rely=0.45, anchor="center")

login_button = tk.Button(root, text="Iniciar Sesión", command=verificar_credenciales, bg=pastel_pink)
login_button.place(relx=0.75, rely=0.55, anchor="center")

root.mainloop()
