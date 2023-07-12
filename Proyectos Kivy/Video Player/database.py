import sqlite3
from video import Video

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
        portada blob,
        route varchar(255)
        """
    )
    conn.commit()
    cur.close()
    conn.close()




def cargar_video(video : Video):
    vid = ({"nombre": video.nombre, "descripcion": video.descripcion, "propietario": video.propietario, "route": video.route})
    conn = sqlite3.connect("VideoPlayer.db")
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO Video(nombre, descripcion, propietario, portada, route) VALUES (?, ?, ?, ?, ?) 
        """, vid)
    conn.commit()
    cur.close()
    conn.close()
    



def listar():
    conn = sqlite3.connect("VideoPlayer.db")
    cur = conn.cursor()
    pass