package strategy

import Polynomial

interface MultiplicationStrategy
{
    fun multiply(p1: Polynomial, p2: Polynomial): Polynomial
}
