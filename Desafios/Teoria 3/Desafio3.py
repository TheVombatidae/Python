#sorted con expresion lambda
def ordenar_nombre(usuarios):
    return sorted(usuarios, key = lambda usuario:usuario[0])

usuarios = [
('JonY BoY', 'Nivel3', 15),
('1962', 'Nivel1', 12),
('caike', 'Nivel2', 1020),
('Straka^', 'Nivel2', 1020),
]

#ord_nom = list(sorted(usuarios,key=lambda usuario:usuario[0])) otra forma

print(ordenar_nombre(usuarios))