# MPI Distributed Polynomial Multiplication

## O(n<sup>2</sup>) Strategy
### Each worker:
* receives the number (numPairs) of (power, coefficient) pairs to multiply by
* receives numPairs pairs of integers
* receives the length (polynomialSize) of the polynomial to multiply
* receives polynomialSize coefficients that make up the polynomial
* computes the partial multiplications and sums them up
* sends the partial result back to the source
### Master:
* computes the first few (power, coefficient) pairs
* adds all the results up by polynomial summation

### Benchmarks:
```text
PROCESS 2: finished in 1 milliseconds
Generated polynomials
2 5 6 5 5 3 8 0 4 7 2 4
7 9 8 9 6 6 6 2 2 7 2 7
Checking:
Expected: 14 53 103 147 185 202 246 241 229 271 266 290 285 225 196 183 95 126 69 64 81 22 28
Computed: 14 53 103 147 185 202 246 241 229 271 266 290 285 225 196 183 95 126 69 64 81 22 28
Result CORRECT, finished in 1 milliseconds
PROCESS 3: finished in 1 milliseconds
PROCESS 1: finished in 1 milliseconds
```

## Karatsuba Strategy
### Each worker:
* receives the length of p1
* receives p1
* receives the length of p2
* receives p2
* receives the first and last powers to compute
* calculates the coefficients
* sends coefficients back
### Master:
* computes the first few coefficients
* places each coefficient calculated into `result`, which represents the result of the multiplication

### Benchmarks:
```text
PROCESS 3: finished in 1 milliseconds
Generated polynomials
7 4 6 5 5 2 8 9 5 3 8 7
3 9 8 9 8 2 4 3 5 0 3 2
Checking:
Expected: 21 75 110 164 200 191 211 249 299 282 326 324 301 259 245 160 108 110 94 54 30 37 14
Computed: 21 75 110 164 200 191 211 249 299 282 326 324 301 259 245 160 108 110 94 54 30 37 14
Result CORRECT, finished in 1 milliseconds
PROCESS 2: finished in 1 milliseconds
PROCESS 1: finished in 1 milliseconds

```

## Hardware specification
* CPU: Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz
* RAM: 64.0 GB