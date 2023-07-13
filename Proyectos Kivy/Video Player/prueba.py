
from database import VideoDAO

vid = VideoDAO()
videos = vid.listar()
for video in videos:
    print(f"Nombre: {video.nombre}  Descripcion: {video.descripcion} Propietario: {video.propietario} Ubicacion: {video.route}")