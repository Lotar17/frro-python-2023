import copy

import kivy
from kivy.app import App
from kivy.uix import videoplayer
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.videoplayer import VideoPlayer
from database import VideoDAO
from video import Video
from pathlib import Path


class ImageButton(ButtonBehavior, BoxLayout):
    pass



class VideoPlayerApp(App):


    def reproducirVideo(self, video : Video):
        app = App.get_running_app()
        app.root.ids.salir.source = video.route
        app.root.current = "player"
        app.root.ids.salir.state = "play"

    def build(self):
        registros = self.findAll()

        self.root.ids.grilla.clear_widgets()


        for registro in registros:
            button = ImageButton()
            button.size_hint = (None, None)
            button.size = (200,200)
            button.orientation = "vertical"
            button.add_widget(Image(source = "ImagenesTPI/mariposa.jpg"))
            button.add_widget(Label(text = registro.nombre))
            button.bind(on_press = lambda *args, registro=registro: self.reproducirVideo(registro))
            self.root.ids.grilla.add_widget(button)

    def defaultPath(self):
        path = Path.home() / "documents" / "videoapp"
        path.mkdir(parents=True, exist_ok=True)
        return str(path)


    def findAll(self):
        videoDB = VideoDAO()
        videos = videoDB.listar()
        return videos

    def videoPlayer(self):
        player = VideoPlayer(source="Videos TPI/rick-astley.mp4")
        player.state = "play"
        player.options = {"eos": "loop"}
        player.alow_stretch = True
        return player



    def cargar_video(self, nombre: str, descripcion: str, propietario: str, route: str):
        video = Video(nombre, descripcion, propietario, route)
        videoDao = VideoDAO()
        videoDao.cargar_video(video)


if __name__ == "__main__":
    VideoPlayerApp().run()
