import BTrees.OOBTree
import ZODB, ZODB.FileStorage
from Persona import Persona
import transaction



class PersonaDAO():

    def cargarPersona(self):
        storage = ZODB.FileStorage.FileStorage("PruebaDB.fs")
        db = ZODB.DB(storage)
        conn = db.open()
        root = conn.root
        root.personas = BTrees.OOBTree.BTree()
        root.personas["Persona-1"] = Persona("222222", "Juan", "Perez", "jperez@hotmail.com")
        transaction.commit()

persona1 = root.personas["Persona-1"]
print(persona1.dni)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.email)







