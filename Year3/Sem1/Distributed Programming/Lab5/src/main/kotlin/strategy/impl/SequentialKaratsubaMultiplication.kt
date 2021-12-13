package strategy.impl

import Polynomial
import strategy.d
import strategy.DEntry
import strategy.MultiplicationStrategy
import kotlin.math.max

class SequentialKaratsubaMultiplication: MultiplicationStrategy {
    override fun multiply(p1: Polynomial, p2: Polynomial): Polynomial {
        val degree = max(p1.degree, p2.degree)
        val n = degree + 1
        val di = (0 until n).map { d(it, p1, p2) }
        val dst = (1 .. 2 * n - 3).associateWith { i ->
            (0 .. i / 2).map { s -> DEntry(s, i - s, p1, p2) }
                .filter { it.s <= degree && it.t <= degree && it.s < it.t }
        }

        val coefficients = (1 until 2 * degree).associateWith { power ->
            val t1 = dst[power]!!.sumOf { it.d }
            val t2 = dst[power]!!.sumOf { di[it.s] + di[it.t] }
            val t3 = if (power % 2 == 0) di[power / 2] else 0

            t1 - t2 + t3
        }.toMutableMap()

        coefficients[0] = di[0]
        coefficients[2 * degree] = di[degree]

        return Polynomial(coefficients.filterValues { it != 0 })
    }
}
