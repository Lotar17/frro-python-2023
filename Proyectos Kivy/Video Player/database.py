import sqlite3

def crear_tabla():

    conn = sqlite3.connect("VideoPlayer.db")
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Video(
        idVideo integer PRIMARY KEY AUTOINCREMENT,
        nombre varchar(30),
        descripcion varchar(255),
        propietario varchar(30),
        portada blob
        """
    )
    conn.commit()
    cur.close()
    conn.close()




def cargar_video(video : Video):
    conn = sqlite3.connect("VideoPlayer.db")
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO Video(nombre, descripcion, propietario, portada) VALUES () 
        """
    )


def listar():
    conn = sqlite3.connect("VideoPlayer.db")
    cur = conn.cursor()
    pass