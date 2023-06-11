"""Base de Datos SQL - Creación de tablas auxiliares"""
import sqlite3

from practico_04.ejercicio_01 import borrar_tabla, crear_tabla


def crear_tabla_peso():
    """Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
        - IdPersona: Int() (Clave Foranea Persona)
        - Fecha: Date()
        - Peso: Int()
    """
    conn = sqlite3.connect("databaseEj4.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS PersonaPeso(
        idPersona integer PRIMARY KEY REFERENCES Persona(idPersona),
        fecha date,
        peso integer,
        )
    """)
    conn.commit()
    cur.close()
    conn.close()


def borrar_tabla_peso():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    conn = sqlite3.connect("databaseEj4.db")
    cur = conn.cursor()
    cur.execute("DROP TABLE PersonaPeso")
    conn.commit()
    cur.close()
    conn.close()


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
