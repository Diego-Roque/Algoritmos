"""
B. T-primes
time limit per test2 seconds
memory limit per test256 megabytes
We know that prime numbers are positive integers that have exactly two distinct positive divisors. Similarly, we'll call a positive integer t Т-prime, if t has exactly three distinct positive divisors.

You are given an array of n positive integers. For each of them determine whether it is Т-prime or not.

Input
The first line contains a single positive integer, n (1 ≤ n ≤ 105), showing how many numbers are in the array. The next line contains n space-separated integers xi (1 ≤ xi ≤ 1012).

Please, do not use the %lld specifier to read or write 64-bit integers in С++. It is advised to use the cin, cout streams or the %I64d specifier.

Output
Print n lines: the i-th line should contain "YES" (without the quotes), if number xi is Т-prime, and "NO" (without the quotes), if it isn't.
"""




import math


def sieve_of_eratosthenes(limit):
    """Generate a list of primes up to the limit using the Sieve of Eratosthenes."""
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return is_prime


def is_t_prime(x, primes):
    """Check if a number x is a T-prime."""
    root = int(math.sqrt(x))
    if root * root == x and primes[root]:
        return True
    return False


def main():
    # Precompute primes up to 10^6
    limit = int(1e6)
    primes = sieve_of_eratosthenes(limit)

    # Input number of elements
    n = int(input())
    numbers = list(map(int, input().split()))

    # Check each number
    results = []
    for x in numbers:
        if is_t_prime(x, primes):
            results.append("YES")
        else:
            results.append("NO")

    # Output results
    print("\n".join(results))


# Run the program
main()
