
import kivy
from kivy.app import App
from kivy.uix import videoplayer
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.videoplayer import VideoPlayer
from database import VideoDAO


class VideoPlayerApp(App):





    def findAll(self):
        videoDB = VideoDAO()
        videos = videoDB.listar()
        return videos

    def generar_grilla(self, grid : GridLayout, button : Button):
        count = self.findAll().count()
        for i in range(count):
            grid.add_widget(button)
        return grid

    def videoPlayer(self):
        player = VideoPlayer(source = "Videos TPI/rick-astley.mp4")
        player.state = "play"
        player.options = {"eos": "loop"}
        player.alow_stretch = True
        return player

if __name__ == "__main__" :
    VideoPlayerApp().run()