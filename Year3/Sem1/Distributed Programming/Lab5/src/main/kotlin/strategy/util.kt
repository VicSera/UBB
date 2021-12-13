package strategy

import Polynomial

private val superscripts = mapOf(
    '0' to '\u2070',
    '1' to '\u00B9',
    '2' to '\u00B2',
    '3' to '\u00B3',
    '4' to '\u2074',
    '5' to '\u2075',
    '6' to '\u2076',
    '7' to '\u2077',
    '8' to '\u2078',
    '9' to '\u2079',
)

fun Int.toPowerString(): String {
    return this.toString().map { superscripts[it] ?: "" }.joinToString("")
}

fun d(power: Int, p1: Polynomial, p2: Polynomial): Int {
    return p1.coefficientForPower(power) * p2.coefficientForPower(power)
}

fun d(coefficient1: Int, coefficient2: Int, p1: Polynomial, p2: Polynomial): Int {
    return (p1.coefficientForPower(coefficient1) + p1.coefficientForPower(coefficient2)) *
            (p2.coefficientForPower(coefficient1) + p2.coefficientForPower(coefficient2))
}

class DEntry(
    val s: Int,
    val t: Int,
    p1: Polynomial,
    p2: Polynomial
) {
    val d = d(s, t, p1, p2)
}
