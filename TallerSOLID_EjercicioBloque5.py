# Python
from enum import Enum

class EstadoTarea(Enum):
    PENDIENTE    = 'pendiente'
    EN_PROGRESO  = 'en progreso'
    TERMINADA    = 'terminada'
    BLOQUEADA    = 'bloqueada'
    EN_REVISION  = 'en_revision'

from estado_tarea import EstadoTarea

class Tarea:
    def __init__(self, nombre, responsable):
        self.nombre = nombre
        self.responsable = responsable
        self.estado = EstadoTarea.PENDIENTE

    def set_estado(self, e: EstadoTarea):
        self.estado = e
