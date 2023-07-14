import sqlite3
from video import Video


class VideoDAO:
    def crear_tabla(self):
        conn = sqlite3.connect("VideoPlayer.db")
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Video(
            idVideo integer PRIMARY KEY AUTOINCREMENT,
            nombre varchar(30),
            descripcion varchar(255),
            propietario varchar(30),
            route varchar(255))
            """)
        conn.commit()
        cur.close()
        conn.close()

    def cargar_video(self, video: Video):
        vid = ({"nombre": video.nombre, "descripcion": video.descripcion, "propietario": video.propietario,
                "route": video.route})
        conn = sqlite3.connect("VideoPlayer.db")
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO Video(nombre, descripcion, propietario, route) VALUES (:nombre, :descripcion, :propietario, :route)",
            vid)
        conn.commit()
        cur.close()
        conn.close()

    def listar(self):
        conn = sqlite3.connect("VideoPlayer.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM Video")
        resultados = cur.fetchall()
        videos = []
        for resultado in resultados:
            idVideo, nombre, descripcion, propietario, route = resultado
            video = Video(idVideo, nombre, descripcion, propietario, route)
            videos.append(video)
        cur.close()
        conn.close()

        return videos

    def borrar_tabla(self):
        conn = sqlite3.connect("VideoPlayer.db")
        cur = conn.cursor()
        cur.execute("DROP TABLE Video")
        conn.commit()
        cur.close()
        conn.close()
