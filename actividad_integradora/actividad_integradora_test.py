import pytest
from longest_prefix_suffix import read_file, two_pointers
from manacher import Manacher
from substring import SubstringFinder

# Prueba para la función two_pointers
@pytest.mark.parametrize(
    "transmission_file, pattern_file, expected",
    [
        ('files/transmission1.txt', 'files/mcode1.txt', False),
        ('files/transmission1.txt', 'files/mcode2.txt', True),
        ('files/transmission1.txt', 'files/mcode3.txt', False),
        ('files/transmission2.txt', 'files/mcode1.txt', True),
        ('files/transmission2.txt', 'files/mcode2.txt', False),
        ('files/transmission2.txt', 'files/mcode3.txt', True),
    ]
)
def test_two_pointers(transmission_file, pattern_file, expected):
    transmission = read_file(transmission_file)
    pattern = read_file(pattern_file)

    result = two_pointers(transmission, pattern)

    assert result == expected

# Prueba para la función manacher_positions
@pytest.mark.parametrize(
    "transmission_file, expected_start, expected_end",
    [
        ('files/transmission1.txt', 66, 68),  # Cambia '66' y '68' por los valores esperados
        ('files/transmission2.txt', 1, 7),    # Cambia '1' y '7' por los valores esperados
    ]
)
def test_manacher_positions(transmission_file, expected_start, expected_end):
    # Lee el archivo de transmisión
    transmission = read_file(transmission_file)

    # Crea una instancia del algoritmo Manacher
    manacher_solver = Manacher()

    # Ejecuta el algoritmo para encontrar la posición inicial y final del palíndromo
    result = manacher_solver.manacher(transmission)

    # Divide el resultado en inicio y fin
    start, end = map(int, result.split())

    # Compara los resultados con los valores esperados
    assert start == expected_start
    assert end == expected_end

@pytest.mark.parametrize(
    "s1, s2, expected_start, expected_end",
    [
        ('files/transmission1.txt', 'files/transmission2.txt', 8, 47),  # Reemplaza por los valores esperados
        # Puedes agregar más casos de prueba si es necesario
    ]
)
def test_longest_common_substring(s1, s2, expected_start, expected_end):
    # Crea una instancia de SubstringFinder
    substring_finder = SubstringFinder(s1, s2)

    # Ejecuta el algoritmo para encontrar la subcadena común más larga
    result = substring_finder.longest_common_substring()

    # Divide el resultado en inicio y fin
    start, end = map(int, result.split())

    # Compara los resultados con los valores esperados
    assert start == expected_start
    assert end == expected_end



if __name__ == "__main__":
    pytest.main()
