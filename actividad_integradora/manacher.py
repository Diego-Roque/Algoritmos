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


class Manacher:
    def manacher(self, transmission: str) -> str:
        """
        Encuentra la subcadena palíndroma más larga utilizando el algoritmo de Manacher.

        Args:
            transmission (str): Nombre del archivo que contiene la transmisión que será procesada.

        Returns:
            str: El rango de índices donde se encuentra el palíndromo más largo en la transmisión original.
                 El formato es: 'inicio fin'.
        """

        # Leer el contenido del archivo de transmisión
        self.transmission: str = transmission

        # Inicializar una lista para almacenar la longitud del palíndromo más largo centrado en cada posición
        palindrome: List[int] = [0] * len(self.transmission)

        # Variables para mantener el centro y el borde derecho del palíndromo actual
        center: int = 0
        right: int = 0

        # Iterar sobre cada carácter en la transmisión
        for idx in range(len(self.transmission)):
            mirror: int = 2 * center - idx  # Índice espejo de la posición actual

            # Verificar si la posición actual está dentro del alcance del palíndromo conocido
            if idx < right:
                palindrome[idx] = min(right - idx, palindrome[mirror])

            # Intentar expandir el palíndromo actual
            while (idx + palindrome[idx] + 1 < len(self.transmission)) and (idx - palindrome[idx] - 1 >= 0) and (
                    self.transmission[idx + palindrome[idx] + 1] == self.transmission[idx - palindrome[idx] - 1]):
                palindrome[idx] += 1

            # Actualizar las variables de centro y borde derecho si el palíndromo actual es más largo
            if idx + palindrome[idx] > right:
                center = idx
                right = idx + palindrome[idx]

        # Encontrar el palíndromo más largo y su centro
        max_length: int = max(palindrome)
        center_index: int = palindrome.index(max_length)

        # Calcular los índices de inicio y fin de la subcadena palíndroma
        start: int = center_index - max_length + 1
        end: int = center_index + max_length + 1

        return f"{start} {end}"


if __name__ == "__main__":
    # Leer el contenido de los dos archivos de transmisión
    transmission1: str = read_file('files/transmission1.txt')
    transmission2: str = read_file('files/transmission2.txt')

    # Crear una instancia del solver de Manacher
    manacher_solver = Manacher()

    # Obtener la posición inicial y final del palíndromo más largo en cada archivo de transmisión
    index1: str = manacher_solver.manacher(transmission1)
    index2: str = manacher_solver.manacher(transmission2)

    # Imprimir los resultados para ambos archivos de transmisión
    print(f"Posición Inicial y Final (transmission1.txt): {index1}")
    print(f"Posición Inicial y Final (transmission2.txt): {index2}")
