'''

This is the most direct implementation of the algorithm called the Sieve of Eratosthenes.

'''

def sieve_classic(n):
    # Check if the input number is less than 2
    if n < 2:
        # Return an empty list since there are no prime numbers less than 2
        return []

    # Initialize a list of boolean values 'True' for all numbers from 0 to n
    prime = [True] * (n + 1)
    # Set the values for 0 and 1 to 'False' as they are not prime numbers
    prime[0] = prime[1] = False

    # Start checking from the first prime number, 2
    p = 2
    # Continue as long as the square of p is less than or equal to n
    while p * p <= n:
        # If prime[p] is still True, then p is a prime number
        if prime[p]:
            # Mark all multiples of p starting from p squared as not prime
            for i in range(p * p, n + 1, p):
                prime[i] = False
        # Move to the next number
        p += 1

    # Initialize an empty list to store the final prime numbers
    primes = []
    # Iterate through the boolean list to collect indices marked as True
    for p in range(n + 1):
        if prime[p]:
            # Add the prime number to the list
            primes.append(p)

    # Return the completed list of prime numbers
    return primes



if __name__ == "__main__":
    # Example
    # Set the upper limit for finding prime numbers
    N = 100
    # Call the function with N and store the result
    prime_numbers = sieve_classic(N)
    # Print the results using a formatted string
    print(f"Prime numbers till {N}:\n{prime_numbers}")