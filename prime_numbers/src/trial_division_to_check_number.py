"""

This script follows the logic: checking for small primes first and stopping at the square root.

"""

def is_prime(n):
    # Step 1. Check the basics
    if n <= 1:
        return False # numbers equal to 1 or less are not primes
    
    if n == 2:
        return True  # 2 is the only even prime
    
    # Step 2. Eliminate even numbers (easy cases)
    if n % 2 == 0:
        return False

    # Step 3 & 4. Find square root and test divisors
    limit = int(n**0.5) + 1
    for divisor in range(3, limit):
        if n % divisor == 0:
            # Step 5. If a divisor is found, it's composite
            return False
            
    # If no divisors were found, it's prime
    return True



if __name__ == "__main__":
    # Example
    test_numbers = [1, 2, 3, 4, 17, 25, 97, 100]
    for num in test_numbers:
        result = is_prime(num)
        print(f"{num}: {result}")
