# Scalar Product
### An implementation of a simple producer-consumer interaction

The app outputs the scalar product of two (hardcoded) vectors.
The implementation is done by using some shared variables:
* the two vectors
* the last computed product
* a mutex
* a condition variable for the mutex

The producer:
* acquires the lock
* checks the condition
    * if the last product was not consumed (is not null), it waits
    * if the last product was consumed (is null), it continues
* computes the new product
* notifies consumer

The consumer:
* initializes the sum with 0
* acquires the lock
* checks the condition
    * if the last product was already consumed (is null), it waits
    * if the last product was not yet consumed (is not null), it continues
* adds the product to the sum
* sets the last product to null
* notifies producer
