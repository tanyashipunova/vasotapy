# Algorithmic complexity

*Keywords: Time complexity, Space complexity*

Time complexity is a theoretical measure, an algorithm growth rate as the size of the input data (n) increases. Instead of measuring actual seconds, it counts the number of elementary operations performed. Time complexity is expressed in Big O notation.

## How to identify in a Python code

### 1. Count the loops
- **No loops (Constant).** If the code performs the same number of steps regardless of input (e.g., accessing a list index `items[0]`), it is $O(1)$.
- **One loop (Linear).** A single loop iterating over the data once (e.g., `for x in my_list:`) is $O(n)$.
- **Nested loops (Quadratic/Cubic).** Two nested loops iterating over the same data result in $O(n^2)$; three nested loops result in $O(n^3)$.
- **Halving data (Logarithmic).** If the code repeatedly halves the data (like Binary Search), it is $O(\log n)$. 

### 2. Account for built-in Python functions
Not all Python functions are $O(1)$. Consider the complexity of internal operations: 
- **$O(1)$:** `len(list)`, `dict` lookups, `list.append()`.
- **$O(n)$:** `list.insert(0, x)`, `list.remove(x)`, `x in list`, list slicing `list[a:b]`.
- **$O(n \log n)$:** Python's built-in sort() or sorted() functions. 

### 3. Apply the rules of simplification
Once you have the total complexity, simplify it using these mathematical rules: 
- **Drop the constants.** $O(2n)$ becomes $O(n)$ because we only care about the growth rate, not the exact number of steps.
- **Keep the dominant term.** In an expression like $O(n^2 + n)$, ignore the lower-order term ($n$) and keep the highest order ($n^2$).
- **Add separate inputs.** If a function iterates over two different lists of sizes $n$ and $m$, the complexity is $O(n + m)$.
