import pytest
from longest_prefix_suffix import read_file, two_pointers
from manacher import Manacher
from substring import SubstringFinder


@pytest.mark.parametrize(
    "transmission_file, pattern_file, expected",
    [
        ('files/transmission1.txt', 'files/mcode1.txt', True),
        ('files/transmission1.txt', 'files/mcode2.txt', False),
        ('files/transmission1.txt', 'files/mcode3.txt', False),
        ('files/transmission2.txt', 'files/mcode1.txt', True),
        ('files/transmission2.txt', 'files/mcode2.txt', True),
        ('files/transmission2.txt', 'files/mcode3.txt', False),
    ]
)
def test_two_pointers(transmission_file, pattern_file, expected):

    transmission = read_file(transmission_file)
    pattern = read_file(pattern_file)


    result = two_pointers(transmission, pattern)


    assert result == expected





if __name__ == "__main__":
    pytest.main()
