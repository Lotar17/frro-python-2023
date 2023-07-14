from video import Video
from database import VideoDAO

videoDB = VideoDAO()

videoDB.borrar_tabla()
videoDB.crear_tabla()
video1 = Video(None,"Rick","Never gonna give you up","Yo", "Videos TPI/rick-astley.mp4")
video2 = Video(None,"Pez", "Pescado girando", "Lotar", r"Videos TPI\fish.mp4")
videoDB.cargar_video(video1)
videoDB.cargar_video(video2)