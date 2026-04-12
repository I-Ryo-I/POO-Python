#Python
def promedio_nivel(self):
    activos = [p for p in self.equipo_principal if p is not None]
    return sum(p.nivel for p in activos) / len(activos) if activos else 0

def imprimir_dungeon(self):
    print('\n=== DUNGEON ===')
    for fila in self.dungeon:
        for celda in fila:
            nombre = celda.nombre if celda is not None else ' vacío '
            print(f'[{nombre:<12}]', end='')
        print()
