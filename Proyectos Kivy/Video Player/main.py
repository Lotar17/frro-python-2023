
import kivy
from kivy.app import App
from kivy.uix import videoplayer
from database import VideoDAO


class VideoPlayerApp(App):

    def findAll(self):
        videoDB = VideoDAO()
        videos = videoDB.listar()
        return videos


if __name__ == "__main__" :
    VideoPlayerApp().run()