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

    def delete_one(self, route: str):
        conn = sqlite3.connect("VideoPlayer.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM Video WHERE route = ?", (route,))
        if cur.rowcount > 0:
            borro = True
        else:
            borro = False
        conn.commit()
        cur.close()
        conn.close()
        return borro


    def getOne(self, route):
        conn = sqlite3.connect("VideoPlayer.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM Video WHERE route = ?", (route,))
        resultado = cur.fetchone()
        if resultado:
            idVideo, nombre, descripcion, propietario, ruta = resultado
            conn.commit()
            video = Video(idVideo, nombre, descripcion, propietario, ruta)
        else:
            video = None
        cur.close()
        conn.close()
        return video

    def updateOne(self,video : Video):
        conn = sqlite3.connect("VideoPlayer.db")
        cur = conn.cursor()
        cur.execute("UPDATE Video SET nombre = ?, descripcion = ?, propietario = ? WHERE route = ?", (video.nombre,video.descripcion, video.propietario, video.route))
        resultado = True if cur.rowcount > 0 else False
        conn.commit()
        cur.close()
        conn.close()
        return resultado

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
