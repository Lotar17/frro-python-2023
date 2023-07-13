from video import Video
from database import VideoDAO

videoDB = VideoDAO()

videoDB.borrar_tabla()
videoDB.crear_tabla()
video1 = Video("Rick","Never gonna give you up","Yo", r"C:\Users\mateo\Documents\videoapp\rick-astley.mp4")
video2 = Video("Pez", "Pescado girando", "Lotar", r"C:\Users\mateo\Documents\videoapp\fish.mp4")
videoDB.cargar_video(video1)
videoDB.cargar_video(video2)