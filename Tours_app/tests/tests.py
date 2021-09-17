import pytest


def prime_factors(n):
    factors = []
    divider = 2
    while n > 1:
        while n % divider == 0:
            factors.append(divider)
            n /= divider
        divider += 1
    return factors


@pytest.mark.parametrize('n, result', (
        (1, []),
        (2, [2]),
        (3, [3]),
        (4, [2, 2]),
        (5, [5]),
        (6, [2, 3]),
        (7, [7]),
        (8, [2, 2, 2]),
        (9, [3, 3]),
        (2 * 2 * 2 * 3 * 3 * 5 * 7 * 11, [2, 2, 2, 3, 3, 5, 7, 11]),
))
def test_prime_factor(n, result):
    assert prime_factors(n) == result