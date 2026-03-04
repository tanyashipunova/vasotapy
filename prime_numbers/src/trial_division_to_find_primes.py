import math

def is_prime_trial_division(num):
    """
    This function checks if a number is prime.
    """
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_trial_division(n):
    """
    This function finds all prime numbers till n.
    """
    primes = []
    for num in range(2, n + 1):
        if is_prime_trial_division(num):
            primes.append(num)
    return primes



if __name__ == "__main__":
    # Example
    N_trial = 100
    prime_numbers_trial = find_primes_trial_division(N_trial)
    print(f"Prime numbers till {N_trial} using trial division method:\n{prime_numbers_trial}")
