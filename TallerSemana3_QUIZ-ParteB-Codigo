class CancionPlaylist:
    def __init__(self, titulo, duracion_seg):
        self.titulo = titulo
        self.duracion_seg = duracion_seg

class Playlist:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__canciones = []                          # lista vacía

    def agregar_cancion(self, titulo, duracion_seg):
        # Composición: crea la canción AQUÍ
        cancion = CancionPlaylist(titulo, duracion_seg)
        self.__canciones.append(cancion)

    def duracion_total_min(self):
        total_seg = sum(c.duracion_seg for c in self.__canciones)
        return round(total_seg / 60, 2)

    def __str__(self):
        return f'Playlist: {self.nombre} | {len(self.__canciones)} canciones | {self.duracion_total_min()} min'
