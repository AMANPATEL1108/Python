from itertools import permutations

def is_prime_rearrangement(num):
    num_str = str(num)
    digits = list(num_str)
    
    # Generate permutations and check for prime
    if generate_permutations(digits):
        return 1
    return 0

def generate_permutations(digits):
    for perm in permutations(digits):
        permutation = int(''.join(perm))
        if is_prime(permutation):
            return True
    return False

def is_prime(n):
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

# Test cases
print(is_prime_rearrangement(910))  # Should print 1
print(is_prime_rearrangement(100))  # Should print 0
