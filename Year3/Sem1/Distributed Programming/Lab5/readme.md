# Polynomial Multiplication
## Multiplies two polynomials (`p1` and `p2`) of different degrees (`n` and `m`) using one of four strategies

### Algorithms:
* O(n<sup>2</sup>): 
  * multiply each element of `p1` with each element of `p2` and collect the result of each operation
* Karatsuba: 
  * compute degree = max(n, m)
  * compute D<sub>i</sub> and D<sub>s,t</sub>
  * go over each power (`i`) from `1` to `2 * degree - 1`
  * to obtain `t1`, sum up each entry of D<sub>s,t</sub>[i]
  * to obtain `t2`, compute the sum D<sub>i</sub>[s] + D<sub>i</sub>[t] for each s, t such that s + t = i
  * `t3` is D<sub>i</sub>[i/2] when `i` is even and 0 when `i` is odd
  * the coefficient for power `i` in the final result will be `t1 - t2 + t3`
  * the coefficient for power `0` is always D<sub>i</sub>[0]
  * the coefficient for power `2 * degree` is always D<sub>i</sub>[degree] 
  
### Strategies:
* Sequential O(n<sup>2</sup>):
  * perform the multiplications sequentially on the main thread
  * result:
    ```text
    Sequential O(n²): 4x¹³ + 14x¹² + 4x¹¹ + 6x⁸ + 29x⁷ + 34x⁶ + 12x⁵ + 24x⁴ + 49x³ + 45x² + 10x
    Strategy Sequential O(n²) took 30 milliseconds to complete
    ```
  * Parallel O(n<sup>2</sup>):
    * for each element of `p1`, get a thread from the thread pool to perform the multiplication with each element of `p2`
    * each thread first computes the partial sum and then adds it to the final result under a mutex lock
    * result (using 3 threads):
    ```text
    Parallel O(n²): 4x¹³ + 14x¹² + 4x¹¹ + 6x⁸ + 29x⁷ + 34x⁶ + 12x⁵ + 24x⁴ + 49x³ + 45x² + 10x
    Strategy Parallel O(n²) took 74 milliseconds to complete
    ```
  * Sequential Karatsuba:
    * the coefficients are all calculated sequentially on the main thread
    * result:
    ```text
    Sequential Karatsuba: 4x¹³ + 14x¹² + 4x¹¹ + 6x⁸ + 29x⁷ + 34x⁶ + 12x⁵ + 24x⁴ + 49x³ + 45x² + 10x
    Strategy Sequential Karatsuba took 5 milliseconds to complete
    ```
  * Parallel Karatsuba:
    * compute each coefficient on a thread from the thread pool
    * add the obtained coefficient to the result coefficients under a mutex lock
    * result (using 3 threads):
    ```text
    Parallel Karatsuba: 4x¹³ + 14x¹² + 4x¹¹ + 6x⁸ + 29x⁷ + 34x⁶ + 12x⁵ + 24x⁴ + 49x³ + 45x² + 10x
    Strategy Parallel Karatsuba took 4 milliseconds to complete
    ```

### Hardware specification
* CPU: Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz
* RAM: 64.0 GB
