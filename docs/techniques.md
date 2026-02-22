# Techniques

## Basic building blocks

- Arrays
- Pointers (in form of array indices, if not memory indices)
- Hashmaps (where keys might act as O(1) pointers)

## Basic actions

- Arrays
  - Iterating array
  - Slicing or indexing array
        In C dereferencing a pointer or indexing an array are synonymous.
  - Appending to array
- Pointers
  - Arithmetic operations

## Language features

- `if-else` selection
  - `elif` is syntactic sugar for chaining two `if-else`
- Iteration using `for` loop
  - `for` should have a `break` or `continue` action. This is syntactic sugar which can be implemented by scoped variables and `if` selection
- Repetition using `while`
  - `while` should have a `break` or `continue` action. This is syntactic sugar which can be implemented by scoped variables and `if` selection

## Techniques

These are common techniques to resolve some issues which might not be intuitive at first.

- Two pointers in 1D array
  - advancing in same direction
  - advancing in different direction
- Iterate  over multiple arrays or collections
- Memoization
- Backtracking
- O(1) lookups through hash tables
