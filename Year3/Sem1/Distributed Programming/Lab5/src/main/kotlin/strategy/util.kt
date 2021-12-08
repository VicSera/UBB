package strategy

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
