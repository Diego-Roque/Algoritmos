def bento(a, b, c, d):
    # Conjunto de todos los restaurantes posibles
    numbers = {1, 2, 3, 4, 5}
    # Conjunto de restaurantes que ya se visitaron
    visit = {a, b, c, d}

    # Obtenemos el restaurante faltante calculando la diferencia
    missing = numbers - visit
    # Retornamos el único elemento que queda en el conjunto 'missing'
    return list(missing)[0]

# Leer la entrada del usuario
a, b, c, d = map(int, input().split())

# Imprimir el resultado
print(bento(a, b, c, d))
