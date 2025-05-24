# First Attempt
```
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
```
# improvement
```
def is_prime(n: int) -> bool:
    """Check if a number is prime.

    This function uses the 6k ± 1 optimization to check for primality, which reduces
    the number of checks needed. It first handles small numbers and eliminates even numbers
    and multiples of 3 early on.
    """
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")

    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True
```
