'''

The Sieve of Eratosthenes. This version uses NumPy library for efficient array operations.

'''

import numpy as np

def sieve_vectorized(limit):
    # If the limit is less than 2, there are no prime numbers
    if limit < 2:
        # Return an empty NumPy array of integers
        return np.array([], dtype=int)

    # Create a boolean array of ones (True) for all numbers up to the limit
    primes_array = np.ones(limit + 1, dtype=bool)
    # Set the values for indices 0 and 1 to False, as they are not prime
    primes_array[0:2] = False

    # Iterate through numbers from 2 up to the square root of the limit
    for p in range(2, int(limit**0.5) + 1):
        # If p is marked as prime, eliminate its multiples
        if primes_array[p]:
            # Use NumPy slicing to set all multiples of p starting from p*p to False
            primes_array[p*p : limit+1 : p] = False

    # Return the indices where it is still True (the prime numbers)
    return np.nonzero(primes_array)[0]



if __name__ == "__main__":
    # Example
    # Set the upper limit for finding prime numbers
    N = 100
    # Call the function with N and store the result
    prime_numbers = sieve_vectorized(N)
    # Print the results using a formatted string
    print(f"Prime numbers till {N}:\n{prime_numbers}")
