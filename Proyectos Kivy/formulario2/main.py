import sqlite3
import datetime

import kivy
from kivy.uix.textinput import TextInput
from kivy.app import App
from practico_04 import ejercicio_01,ejercicio_02





class Formulario2App(App):

    def buscar(self, nombre : str):
        if nombre == self.buscar_persona(nombre):
            return "Entraste con exito"
        return "No entraste con exito"

    def buscar_persona(self, name: str):
        """Implementar la funcion buscar_persona, que devuelve el registro de una
        persona basado en su id. El return es una tupla que contiene sus campos:
        id, nombre, nacimiento, dni y altura. Si no encuentra ningun registro,
        devuelve False."""
        conn = sqlite3.connect("databaseEj4.db")
        cur = conn.cursor()
        res = cur.execute("SELECT * FROM Persona WHERE Nombre = ?", (name,)).fetchone()
        nombre = res
        resultado = nombre
        print(resultado)
        conn.commit()
        cur.close()
        conn.close()
        return resultado if resultado is not None else None



if __name__ == "__main__":
    ejercicio_01.crear_tabla()
    ejercicio_02.agregar_persona("Lotar", datetime.datetime(1988, 5, 15), 43576573, 190)
    ejercicio_02.agregar_persona("aaa", datetime.datetime(1988, 5, 15), 43576573, 190)
    Formulario2App().run()