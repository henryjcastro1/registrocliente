import sqlite3

def crear_tabla_servicios():
    try:
        conexion = sqlite3.connect('servicios.db')
        cursor = conexion.cursor()

        # Crear la tabla 'registros_servicios' si no existe
        cursor.execute('''CREATE TABLE IF NOT EXISTS registros_servicios (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            opcion1 INTEGER,
                            opcion2 INTEGER,
                            opcion3 INTEGER,
                            opcion4 INTEGER,
                            opcion5 INTEGER,
                            opcion6 INTEGER,
                            opcion7 INTEGER,
                            opcion8 INTEGER,
                            total REAL,
                            fecha TEXT
                        )''')

        conexion.commit()
        print("Tabla 'registros_servicios' creada correctamente.")

    except sqlite3.Error as error:
        print("Error al conectar a la base de datos SQLite:", error)
    finally:
        if conexion:
            conexion.close()

def registrar(opciones, total, fecha):
    try:
        # Conectar con la base de datos
        conexion = sqlite3.connect('servicios.db')
        cursor = conexion.cursor()

        # Insertar los valores en la base de datos
        cursor.execute("INSERT INTO registros_servicios (opcion1, opcion2, opcion3, opcion4, opcion5, opcion6, opcion7, opcion8, total, fecha) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       (*opciones, total, fecha))

        conexion.commit()
        print("Datos registrados exitosamente.")

    except sqlite3.Error as error:
        print("Error al conectar a la base de datos SQLite:", error)
    finally:
        if conexion:
            conexion.close()

if __name__ == "__main__":
    crear_tabla_servicios()
