import strategy.toPowerString

data class Polynomial(val coefficientMap: Map<Int, Int>) {
    val maxPower = coefficientMap.keys.maxOrNull() ?: 0

    fun multiplyByElement(coefficient: Int, power: Int): Polynomial {
        val coefficients = coefficientMap.map { elem -> (elem.key + power) to (elem.value * coefficient) }.toMap()
        return Polynomial(coefficients)
    }

    fun add(other: Polynomial): Polynomial {
        val coefficients = (coefficientMap.asSequence() + other.coefficientMap.asSequence())
            .groupBy ({it.key}, {it.value})
            .mapValues { (_, coefficients) -> coefficients.sum() }

        return Polynomial(coefficients)
    }

    override fun toString(): String
    {
        return coefficientMap
            .map { (power, coefficient) -> "$coefficient" +
                    (if (power != 0) "x" else "") +
                    if (power > 1) power.toPowerString() else ""
            }
            .joinToString(" + ")
    }
}
