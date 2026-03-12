class Mesa:
    def __init__(self, color, material):
        self.color = color
        self.material = material
        
    def sostener(self, objeto):
        print(f'Este objeto {objeto} Esta encima de la mesa')
        
    def apoyar(self, tareas):
        print(f'Estoy haciendo {tareas} En la mesa')
        
mesa = Mesa('Amarillo', 'Plastico')
mesa.sostener('Computador')
mesa.apoyar('Taller de Python')
    

    