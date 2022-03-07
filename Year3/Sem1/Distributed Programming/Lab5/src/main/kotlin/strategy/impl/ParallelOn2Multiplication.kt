package strategy.impl

import Polynomial
import kotlinx.coroutines.asCoroutineDispatcher
import kotlinx.coroutines.async
import kotlinx.coroutines.job
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking
import kotlinx.coroutines.sync.Mutex
import kotlinx.coroutines.sync.withLock
import strategy.MultiplicationStrategy
import java.util.concurrent.Executors

class ParallelOn2Multiplication(private val nThreads: Int): MultiplicationStrategy
{
    override fun multiply(p1: Polynomial, p2: Polynomial): Polynomial
    {
        val pool = Executors.newFixedThreadPool(nThreads).asCoroutineDispatcher()
        var result = Polynomial()
        val mutex = Mutex()

        runBlocking {
            p1.coefficientMap.forEach { (power, coefficient) ->
                launch (pool) {
                    val partialSum = p2.multiplyByElement(coefficient, power)

                    mutex.withLock {
                        result = result.add(partialSum)
                    }
                }
            }
        }

        return result
    }

    override fun toString(): String {
        return "Parallel O(n\u00B2)"
    }
}
