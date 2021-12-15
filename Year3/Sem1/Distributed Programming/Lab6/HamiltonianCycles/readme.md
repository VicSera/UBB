# Hamiltonian Cycles
## Find a hamiltonian cycle in a graph

### Strategies
* Sequential ([SequentialHamiltonianCycleFinder](src/main/kotlin/strategy/impl/SequentialHamiltonianCycleFinder.kt))
  * iterative depth-first-search using a stack containing (path, node) pairs, denoting the current path and the current node to process
  * at each iterative step, look through the neighbors of the current node:
    * if neighbor is the starting node and the current path contains all nodes, then by adding the starting node again we obtain a Hamiltonian cycle and return it
    * otherwise, if the neighbor is not already in the current path, push the current path and the neighbor to the stack
  * stop search forcibly if the stack is empty 
  * execution:
  ```text
  0 -> 1 -> 2 -> 3 -> 4 -> 0
  Sequential Hamiltonian Cycle Finder took 4 milliseconds
  ```
* Parallel ([SequentialHamiltonianCycleFinder](src/main/kotlin/strategy/impl/ParallelHamiltonianCycleFinder.kt))
  * iterative depth-first-search like in the `Sequential` strategy
  * at each iterative step, looks through the neighbors of the current node using multiple threads,
  but in case a cycle is found, don't immediately return it, but save it in `result`
  * stop forcibly if either the stack is empty or `result` is set
  * execution:
  ```text
  0 -> 1 -> 2 -> 3 -> 4 -> 0
  Parallel Hamiltonian Cycle Finder took 68 milliseconds
  ```
  
### Hardware specification
* CPU: Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz
* RAM: 64.0 GB
