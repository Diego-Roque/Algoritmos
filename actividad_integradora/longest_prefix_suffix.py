from typing import List


def read_file(file_path: str) -> str:
    """
    Lee el contenido de un archivo y lo devuelve como una cadena de texto.

    Args:
        file_path (str): Ruta al archivo que se desea leer.

    Returns:
        str: El contenido del archivo como una cadena de texto.
    """
    with open(file_path, 'r') as file:
        return file.read().strip()


def lps(pattern: str) -> List[int]:
    """
    Calcula el array LPS (Longest Prefix Suffix) para el patrón dado.

    Args:
        pattern (str): El patrón para el cual se calculará el array LPS.

    Returns:
        List[int]: Un array que contiene la longitud del prefijo más largo que es también sufijo en cada posición del patrón.
    """
    n: int = len(pattern)
    lps_arr: List[int] = [0] * n  # Inicializamos el array de LPS con ceros
    length: int = 0  # Longitud del prefijo más largo que es también sufijo
    i: int = 1

    while i < n:
        if pattern[i] == pattern[length]:
            length += 1
            lps_arr[i] = length
            i += 1
        else:
            if length != 0:
                length = lps_arr[length - 1]  # Retrocedemos
            else:
                lps_arr[i] = 0
                i += 1
    return lps_arr


def two_pointers(transmission: str, pattern: str) -> bool:
    """
    Utiliza el algoritmo de KMP (Knuth-Morris-Pratt) para buscar si el patrón está presente en la transmisión.

    Args:
        transmission (str): La cadena en la cual se buscará el patrón.
        pattern (str): El patrón a buscar en la transmisión.

    Returns:
        bool: True si el patrón es encontrado en la transmisión, False en caso contrario.
    """
    prefix: List[int] = lps(pattern)
    m: int = len(transmission)
    n: int = len(pattern)

    i: int = 0  # Índice para la transmisión
    j: int = 0  # Índice para el patrón

    while i < m:
        if transmission[i] == pattern[j]:
            i += 1
            j += 1

        if j == n:  # Si encontramos el patrón completo
            return True  # El patrón fue encontrado

        # Mismatch después de j matches
        elif i < m and transmission[i] != pattern[j]:
            if j != 0:
                j = prefix[j - 1]  # Retrocedemos usando el array LPS
            else:
                i += 1

    return False  # Si no encontramos el patrón


if __name__ == "__main__":
    # Leer el archivo de transmisión y el archivo de patrón
    transmission: str = read_file('transmission1.txt')
    pattern: str = read_file('mcode1.txt')

    # Verificar si el patrón está contenido en la transmisión
    result: bool = two_pointers(transmission, pattern)

    # Imprimir el resultado (True o False)
    print(result)
