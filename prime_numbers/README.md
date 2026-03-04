# Prime numbers

A prime number has exactly two factors: 1 and itself. If you find a number (other than 1 and itself) that divides into it without a remainder, it isn't prime.

**Example. Primes till 100**
```
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```

## How to check whether a number is prime

|Solution|Example in Python|Time complexity|
|:---|:---|:---|
|The Trial Division. To check a number|[trial_division_to_check_number.py](./src/trial_division_to_check_number.py)|$O(\sqrt{n})$|
||||

### Trial Division

The Trial Division method is the most straightforward way to check if a number is prime. It is based on a simple logic: try dividing the number by smaller numbers to see if any fit perfectly.

To save time, don't test every single number. Follow these three rules:
- Stop at the square root. If a number has a factor, one of those factors must be less than or equal to $\sqrt{n}$. Example: to check 31, the square root is about 5.5. Hence, check numbers up to 5.
- Only test primes. No need to test 4, 6, or 8. If 2 doesn't divide into the number, 4 certainly won't either.
- Check the "easy" primes first. Most composite numbers are divisible by 2, 3, or 5.

## How to get all prime numbers till N

|Solution|Example in Python|Time complexity|
|:---|:---|:---|
|The Trial Division. To find prime numbers|[trial_division_to_find_primes.py](./src/trial_division_to_find_primes.py)|$O(n \sqrt{n})$|
|The Sieve of Eratosthenes. Classic|[sieve_classic.py](./src/sieve_classic.py)|$O(n \log \log n)$|
|The Sieve of Eratosthenes. Vectorized|[sieve_vectorized.py](./src/sieve_vectorized.py)|$O(n \log \log n)$|

### The Sieve of Eratosthenes

The Sieve of Eratosthenes is an ancient algorithm for finding all prime numbers up to a given limit `n`. It works by iteratively marking the multiples of each prime number starting from 2. The numbers that remain unmarked at the end of the process are the prime numbers.

There are different implementations of the same core algorithm - the Sieve of Eratosthenes:
1. Classic Sieve. In this version:
- the `while (p * p <= n)` loop stops the check as soon as the square of the current number exceeds the $N$ limit
- final collection of results via a loop with `.append()`
2. Vectorized Sieve. This version:
- uses NumPy library focusing on its "vectorized" nature
- is significantly faster for large limits because it uses vectorized slicing instead of an inner Python loop
