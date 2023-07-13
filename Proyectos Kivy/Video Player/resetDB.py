from video import Video
from database import VideoDAO

videoDB = VideoDAO()

videoDB.borrar_tabla()
videoDB.crear_tabla()
video1 = Video("Rick","Never gonna give you up","Yo", "/home/lkblkb/VideosTPI/rick-astley-never-gonna-give-you-up-official-music-video.mp4")
video2 = Video("Pez", "Pescado girando", "Lotar", r"Videos TPI\fish.mp4")
videoDB.cargar_video(video1)
videoDB.cargar_video(video2)