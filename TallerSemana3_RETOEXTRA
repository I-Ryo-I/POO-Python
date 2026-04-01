class Docente:
    def __init__(self, nombre, titulo):
        self.nombre = nombre
        self.titulo = titulo
        self.__cursos = []

    def asignar_curso(self, curso):
        if self.calcular_carga() + curso._Curso__creditos <= 16:
            self.__cursos.append(curso)
        else:
            print("No puede superar 16 creditos")

    def calcular_carga(self):
        return sum(c._Curso__creditos for c in self.__cursos)
