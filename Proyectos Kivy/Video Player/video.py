from moviepy.editor import VideoFileClip
from PIL import Image as Image


class Video:
    def __init__(self, nombre=None, descripcion=None, propietario=None, route=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.propietario = propietario
        self.route = route
        self.thumb = self.setThumbnail()

    def setThumbnail(self):
        clip = VideoFileClip(self.route)
        frame = clip.get_frame(10)
        clip.close()
        thumbnail = Image.fromarray(frame)
        thumbnail = thumbnail.resize((320, 240), reducing_gap=True)
        return thumbnail
