from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label

from database import VideoDAO
from main import ImageButton


class MyApp(App):
    def build(self):
        vid = VideoDAO()
        # Simulación de registros de base de datos
        registros = vid.listar()

        grid = GridLayout(cols=4, size_hint_y = 0.9, spacing = 20)

        for registro in registros:
            button = ImageButton()
            button.size_hint = (None, None)
            button.size = (200,200)
            button.orientation = "vertical"
            button.add_widget(Image(source="ImagenesTPI/mariposa.jpg"))
            button.add_widget(Label(text = registro.nombre))
            grid.add_widget(button)

        return grid


if __name__ == "__main__":
    MyApp().run()
