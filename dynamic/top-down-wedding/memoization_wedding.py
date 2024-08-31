from typing import List
def wedding_memoization(budget: int, garment_count: int, prices: List[List[int]]) -> int:
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


    # Crear una tabla para memoization
    memo = [[-1 for _ in range(budget + 1)] for _ in range(garment_count + 1)]

    # Función auxiliar que realiza el cálculo con memoization
    def dp(g_index: int, remaining_budget: int) -> int:
        # Caso base: si hemos procesado todos los artículos de ropa
        if g_index == garment_count:
            # Si hemos gastado exactamente el presupuesto, devolver 0 (éxito)
            return 0 if remaining_budget == 0 else -float('inf')

        # Si ya hemos calculado esta subsolución, la devolvemos
        if memo[g_index][remaining_budget] != -1:
            return memo[g_index][remaining_budget]

        # Iniciar con un valor alto negativo para maximizar
        result = -float('inf')

        # Intentar comprar cada opción para la prenda actual
        for price in prices[g_index]:
            if remaining_budget >= price:
                # Llamada recursiva a la siguiente prenda
                result = max(result, dp(g_index + 1, remaining_budget - price))

        # Guardar la mejor opción en memo
        memo[g_index][remaining_budget] = result
        return result

    # Iniciar el proceso de memoization
    best_value = dp(0, budget)

    # Si el valor exacto puede ser alcanzado, retornar 0
    if best_value == 0:
        return 0
    # Si se puede gastar una cantidad dentro del presupuesto pero no exacta, devolver la diferencia
    elif best_value != -float('inf'):
        return budget - best_value
    # Si no se pudo gastar el presupuesto, se retorna -1
    else:
        return -1
