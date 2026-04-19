# Python
def subir_nivel(self):
    self.nivel += 1
    self.hp += 10

for p in equipo:
    if p is not None and p.nivel < 10:
        p.subir_nivel()
