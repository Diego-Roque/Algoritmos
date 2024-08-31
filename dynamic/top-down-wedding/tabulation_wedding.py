from typing import List, Union


def wedding_tabulation(budget: int, garment_count: int, prices: List[List[int]]) -> Union[int, float]:
    """
    Calcula la cantidad mínima de presupuesto sobrante después de comprar exactamente una prenda de cada tipo.

    Args:
        budget (int): El presupuesto total disponible.
        garment_count (int): El número de tipos de prendas disponibles.
        prices (List[List[int]]): Una lista de listas, donde cada sublista contiene los precios de las opciones de cada tipo de prenda.

    Returns:
        int: El presupuesto sobrante mínimo si es posible comprar una prenda de cada tipo sin exceder el presupuesto.
             Si no es posible comprar una prenda de cada tipo dentro del presupuesto, devuelve -1.
             Si se gasta exactamente el presupuesto, devuelve 0.
    """

    # Crear una tabla para tabulación: dp[garment_index][remaining_budget]
    dp = [[-float('inf')] * (budget + 1) for _ in range(garment_count + 1)]

    # Caso base: se inicia sin haber comprado nada, así que el presupuesto restante es igual al presupuesto total
    dp[0][budget] = 0

    # Rellenar la tabla de tabulación
    for g_index in range(1, garment_count + 1):
        for remaining_budget in range(budget + 1):
            if dp[g_index - 1][remaining_budget] != -float('inf'):
                for price in prices[g_index - 1]:
                    if remaining_budget >= price:
                        dp[g_index][remaining_budget - price] = max(dp[g_index][remaining_budget - price], dp[g_index - 1][remaining_budget] + price)

    # Encontrar el valor máximo utilizado que no exceda el presupuesto
    best_value = max(dp[garment_count])

    # Si el valor exacto puede ser alcanzado, retornar 0
    if best_value == budget:
        return 0
    # Si se puede gastar una cantidad dentro del presupuesto pero no exacta, devolver la diferencia
    elif best_value != -float('inf'):
        return budget - best_value
    # Si no se pudo gastar el presupuesto, se retorna -1
    else:
        return -1
