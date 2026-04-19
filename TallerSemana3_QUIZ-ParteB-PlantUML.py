@startuml
class Playlist {
  - nombre: String
  - canciones: List<CancionPlaylist>
  + agregar_cancion(titulo, duracion): void
  + duracion_total_min(): float
}

class CancionPlaylist {
  - titulo: String
  - duracion_seg: int
}

Playlist *-- "1..*" CancionPlaylist : contiene >
@enduml
