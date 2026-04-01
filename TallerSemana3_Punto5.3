class Programa:
    def __init__(self, nombre, snies):
        self.nombre = nombre
        self.snies = snies
        self.__cursos = []     # composición con Curso
        self.__docentes = []   # agregación con Docente

    def agregar_curso(self, curso):
        self.__cursos.append(curso)
        print(f'Curso {curso.nombre} agregado a {self.nombre}')

    def vincular_docente(self, docente):
        self.__docentes.append(docente)
        print(f'Docente {docente.nombre} vinculado a {self.nombre}')

    def total_estudiantes(self):
        # Suma los matriculados en todos los cursos
        return sum(len(curso._Curso__estudiantes) for curso in self.__cursos)

    def __str__(self):
        return f'Programa: {self.nombre} | SNIES: {self.snies} | Cursos: {len(self.__cursos)}'


class Universidad:
    def __init__(self, nombre, ciudad):
        self.__nombre = nombre
        self.__ciudad = ciudad
        self.__programas = []   # composición con Programa

    def crear_programa(self, nombre, snies):
        prog = Programa(nombre, snies)
        self.__programas.append(prog)
        print(f'Programa {nombre} creado en {self.__nombre}')
        return prog

    def listar_programas(self):
        print(f'--- Programas de {self.__nombre} ({self.__ciudad}) ---')
        for p in self.__programas:
            print(f'  {p}')

    def buscar_programa(self, nombre):
        return next((p for p in self.__programas if p.nombre == nombre), None)
