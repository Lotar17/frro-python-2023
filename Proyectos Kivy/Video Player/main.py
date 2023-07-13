import kivy
from kivy.app import App
from kivy.uix import videoplayer
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.recycleview import RecycleView
from kivy.uix.videoplayer import VideoPlayer
from database import VideoDAO
from pathlib import Path


class VideoItem(BoxLayout):
    def __init__(self, video, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 100
        self.video = video


class VideoList(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = []

    def refresh_view_attrs(self, rv, index, data):
        video = data['video']
        return {'video': video}


class VideoPlayerApp(App):

    def defaultPath(self):
        path = Path.home() / "documents" / "videoapp"
        path.mkdir(parents=True, exist_ok=True)
        return str(path)

    def findAll(self):
        videoDB = VideoDAO()
        videos = videoDB.listar()
        return videos

    def generar_grilla(self, video_list: VideoList):
        videos = self.findAll()
        count = videos.count()
        for video in videos:
            video_item = VideoItem(video=video)
            video_list.data.append({'video': video_item})

    def videoPlayer(self):
        player = VideoPlayer(source="Videos TPI/rick-astley.mp4")
        player.state = "play"
        player.options = {"eos": "loop"}
        player.alow_stretch = True
        return player


if __name__ == "__main__":
    VideoPlayerApp().run()
