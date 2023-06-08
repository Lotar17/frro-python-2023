"""Base de Datos SQL - Alta"""

import datetime
import sqlite3

from practico_04.ejercicio_01 import reset_tabla


def agregar_persona(nombre, nacimiento, dni, altura):
    """Implementar la funcion agregar_persona, que inserte un registro en la 
    tabla Persona y devuelva los datos ingresados el id del nuevo registro."""
    persona = ({"nombre": nombre, "nacimiento": nacimiento, "dni": dni, "altura": altura })
    conn = sqlite3.connect("databaseEj4.db")
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO Persona(nombre,fechaNacimiento,dni,altura) VALUES (:nombre, :nacimiento, :dni, :altura)
    """, persona)
    id_persona = cur.lastrowid
    conn.commit()
    cur.close()
    conn.close()
    return id_persona


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
