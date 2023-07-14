


class Video:

    def __init__(self, idVideo=None, nombre=None, descripcion=None, propietario=None, route=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.propietario = propietario
        self.route = route
        self.idVideo = idVideo
    ##     self.thumb = self.setThumbnail()    SETEAR FRAME DEL VIDEO


"""
    def setThumbnail(self):
        clip = VideoFileClip(self.route)
        frame = clip.get_frame(10)
        clip.close()
        thumbnail = Image.fromarray(frame)
        thumbnail = thumbnail.resize((320, 240), reducing_gap=True)
        return thumbnail
"""
