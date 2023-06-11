"""Base de Datos SQL - Búsqueda"""

import datetime
import sqlite3

from practico_04.ejercicio_01 import reset_tabla
from practico_04.ejercicio_02 import agregar_persona


def buscar_persona(id_persona):
    """Implementar la funcion buscar_persona, que devuelve el registro de una 
    persona basado en su id. El return es una tupla que contiene sus campos: 
    id, nombre, nacimiento, dni y altura. Si no encuentra ningun registro, 
    devuelve False."""
    conn = sqlite3.connect("databaseEj4.db")
    cur = conn.cursor()
    res = cur.execute("SELECT * FROM Persona per WHERE idPersona = ?", (id_persona,)).fetchone()
    idper, nombre, nac, dni, altura = res
    nac = datetime.datetime.strptime(nac, "%Y-%m-%d %H:%M:%S")
    print(res)
    resultado = (idper, nombre, nac, dni, altura)
    print(resultado)
    conn.commit()
    cur.close()
    conn.close()

    return resultado if resultado is not None else None



# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
