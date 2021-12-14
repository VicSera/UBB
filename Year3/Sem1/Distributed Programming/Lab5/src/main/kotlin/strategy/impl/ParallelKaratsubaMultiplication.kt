package strategy.impl

import Polynomial
import kotlinx.coroutines.asCoroutineDispatcher
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking
import kotlinx.coroutines.sync.Mutex
import kotlinx.coroutines.sync.withLock
import strategy.DEntry
import strategy.MultiplicationStrategy
import strategy.computeCoefficient
import strategy.d
import java.util.concurrent.Executors
import kotlin.math.max

class ParallelKaratsubaMultiplication(private val nThreads: Int): MultiplicationStrategy {
    override fun multiply(p1: Polynomial, p2: Polynomial): Polynomial {
        val mutex = Mutex()
        val pool = Executors.newFixedThreadPool(nThreads).asCoroutineDispatcher()

        val degree = max(p1.degree, p2.degree)
        val n = degree + 1
        val di = (0 until n).map { d(it, p1, p2) }
        val dst = (0 .. 2 * n - 3).map { i ->
            (0 .. i / 2).map { s -> DEntry(s, i - s, p1, p2) }
                .filter { it.s <= degree && it.t <= degree && it.s < it.t }
        }
        val coefficients = mutableMapOf<Int, Int>()

        runBlocking {
            (1 until 2 * degree).forEach { power ->
                launch(pool) {
                    computeCoefficient(power, di, dst)
                        .takeIf { it != 0 }
                        ?.let {
                            mutex.withLock {
                                coefficients[power] = it
                            }
                        }
                }
            }
        }

        coefficients[0] = di[0]
        coefficients[2 * degree] = di[degree]

        return Polynomial(coefficients.filterValues { it != 0 })
    }

    override fun toString(): String {
        return "Parallel Karatsuba"
    }
}
