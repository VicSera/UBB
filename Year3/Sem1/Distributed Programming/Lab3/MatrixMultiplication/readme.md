# Matrix Multiplication
## Compute the product of two `n*n` matrices using `t` threads

## Hardware specification:
* CPU: Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz
* RAM: 64.0 GB

## Approaches
* Sequential on rows (`SOR`) - each thread has a different starting point (evenly distributed across the matrix) and computes the
product cell by cell, incrementing columns first, then rows
* Sequential on columns (`SOC`) - each thread has a different starting point (evenly distributed across the matrix) and computes the
  product cell by cell, incrementing rows first, then columns
* Skip N (`SN`) - each thread (numbered by `t'`) starts at the `t'`<sup>th</sup> element and skips `t - 1` elements

## Benchmarks
### Time is measured in milliseconds
#### Using a thread pool:
* `n` = 9, `t` = 4:
  * `SOR`: 98
  * `SOC`: 105
  * `SN`: 84
* `n` = 20, `t` = 5:
  * `SOR`: 95
  * `SOC`: 100
  * `SN`: 132
* `n` = 50, `t` = 2:
  * `SOR`: 187
  * `SOC`: 203
  * `SN`: 193
#### Using a thread list:
* `n` = 9, `t` = 4:
  * `SOR`: 11
  * `SOC`: 11
  * `SN`: 14
* `n` = 20, `t` = 5:
  * `SOR`: 30
  * `SOC`: 27
  * `SN`: 33
* `n` = 50, `t` = 2:
  * `SOR`: 79
  * `SOC`: 85
  * `SN`: 80
