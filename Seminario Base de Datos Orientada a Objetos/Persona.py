import persistent

class Persona(persistent.Persistent):

    def __init__(self, dni : str, nombre : str, apellido : str, email : str):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def cambiarEmail(self, email : str):
        self.email = email
