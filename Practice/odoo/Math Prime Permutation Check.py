def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_permutations(s, prefix, seen):
    if len(s) == 0:
        number = int(prefix)
        if is_prime(number):
            return True
    else:
        for i in range(len(s)):
            new_prefix = prefix + s[i]
            new_str = s[:i] + s[i+1:]
            if new_prefix not in seen:
                seen.add(new_prefix)
                if generate_permutations(new_str, new_prefix, seen):
                    return True
    return False

def MathChallenge(num):
    # Check if any permutation of num is prime
    return 1 if generate_permutations(str(num), "", set()) else 0

# Test cases
print(MathChallenge(98))   # Output: 1
print(MathChallenge(598))  # Output: 1
print(MathChallenge(910))  # Output: 1
print(MathChallenge(123))  # Output: 0
