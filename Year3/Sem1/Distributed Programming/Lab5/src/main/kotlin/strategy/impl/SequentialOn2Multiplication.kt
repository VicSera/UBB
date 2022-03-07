package strategy.impl

import Polynomial
import strategy.MultiplicationStrategy

class SequentialOn2Multiplication: MultiplicationStrategy
{
    override fun multiply(p1: Polynomial, p2: Polynomial): Polynomial
    {
        return p1.coefficientMap.map { (power, coefficient) -> p2.multiplyByElement(coefficient, power) }
            .reduce { acc, polynomial -> acc.add(polynomial) }
    }

    override fun toString(): String {
        return "Sequential O(n\u00B2)"
    }
}
