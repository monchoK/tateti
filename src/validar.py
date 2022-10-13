# Valida el id (si es numérico y de longitud 6).
def validar_id(id: str) -> bool:
    return (id.isnumeric() and len(id) <= 6)

# Valida el nombre (si es un texto sin espacios en blanco de entre 1 y 30 caracteres).
def validar_names(names: str) -> bool:
    names = names.strip()
    return (len(names) > 0 and len(names) <= 30)

# Valida que los puntos estén entre 1 y 99.
def validar_points(points: str) -> bool:
    points_texto = str(points)
    if points_texto.isnumeric():
        return (int(points) >= 1 and int(points) <= 99)
    else:
        return False