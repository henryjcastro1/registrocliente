import sqlite3

def crear_tabla_clientes():
    try:
        conexion = sqlite3.connect('clientes.db')
        cursor = conexion.cursor()

        # Crear la tabla 'clientes' si no existe
        cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                            id INTEGER PRIMARY KEY,
                            nombre TEXT,
                            apellido TEXT,
                            documento TEXT,
                            telefono TEXT,
                            direccion TEXT,
                            correo TEXT
                        )''')

        conexion.commit()
        print("Tabla 'clientes' creada correctamente.")

    except sqlite3.Error as error:
        print("Error al conectar a la base de datos SQLite:", error)
    finally:
        if conexion:
            conexion.close()

if __name__ == "__main__":
    crear_tabla_clientes()