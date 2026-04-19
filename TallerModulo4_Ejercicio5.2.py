# Python -- TU CÓDIGO AQUÍ
g = GremioRPG('Avengers')

p1 = Personaje('Thor', 12, 130)
p2 = Personaje('Wanda', 9, 100)
p3 = Personaje('IronMan', 20, 200)
p4 = Personaje('Spiderman', 5, 70)
p5 = Personaje('CapitanAmerica', 8, 110)
p6 = Personaje('Hulk', 18, 95)
p7 = Personaje('DoctorStrange', 4, 65)
p8 = Personaje('PanteraNegra', 18, 180)

for p in [p1, p2, p3, p4, p5, p6, p7, p8]:
    g.unirse_al_equipo(p)

g.colocar_en_dungeon(p1, 0, 0)
g.colocar_en_dungeon(p3, 1, 1)
g.colocar_en_dungeon(p5, 2, 0)
g.colocar_en_dungeon(p2, 0, 2)

p4.hp = 0
p6.hp = 0
g.limpiar_caidos()
g.reporte_gremio()
