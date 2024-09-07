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


class SubstringFinder:
    def __init__(self, s1: str = "files/transmission1.txt", s2: str = "files/transmission2.txt"):
        """
        Inicializa el contenido de los dos archivos de transmisión para buscar la subcadena común más larga.

        Args:
            s1 (str): Ruta del primer archivo de transmisión.
            s2 (str): Ruta del segundo archivo de transmisión.
        """
        self.s1: str = read_file(s1)
        self.s2: str = read_file(s2)

    def longest_common_substring(self) -> str:
        """
        Encuentra la subcadena común más larga entre las dos transmisiones.

        Returns:
            str: Las posiciones inicial y final de la subcadena común más larga en la primera transmisión (1-based index).
        """
        # Inicializar la tabla de programación dinámica (DP)
        dp: List[List[int]] = [[0] * (len(self.s2) + 1) for _ in range(len(self.s1) + 1)]

        max_length = 0  # Longitud de la subcadena común más larga
        end_index_s1 = 0  # Índice de finalización de la subcadena en s1

        # Llenar la tabla DP
        for i in range(1, len(self.s1) + 1):
            for j in range(1, len(self.s2) + 1):
                if self.s1[i - 1] == self.s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > max_length:
                        max_length = dp[i][j]
                        end_index_s1 = i
                else:
                    dp[i][j] = 0

        # Calcular la posición inicial (1-based index)
        start_index_s1 = end_index_s1 - max_length + 1

        return f"{start_index_s1} {end_index_s1}"


if __name__ == "__main__":
    # Crear una instancia de SubstringFinder y ejecutar la búsqueda de la subcadena común más larga
    substring_finder = SubstringFinder()

    # Obtener la posición inicial y final de la subcadena común más larga
    result: str = substring_finder.longest_common_substring()

    # Imprimir el resultado
    print(f"Posición Inicial y Final en la transmisión 1: {result}")
