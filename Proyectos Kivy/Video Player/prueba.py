from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.videoplayer import VideoPlayer

class MainApp(MDApp):
    title = "Simple video"
    def build(self):
        player = VideoPlayer(source = 'Videos TPI/rick-astley.mp4')
        player.state = "play"
        player.options = {"eos" : "loop"}
        player.allow_fullscreen = True
        return player

MainApp().run()