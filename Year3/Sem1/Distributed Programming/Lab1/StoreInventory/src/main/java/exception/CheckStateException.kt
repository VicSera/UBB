package exception

abstract class CheckStateException(
    val prefix: String,
    val subject: String?,
    val expected: String,
    val actual: String
) : Exception() {
    override fun toString(): String {
        return prefix + (if (subject != null) "($subject) " else "") + "expected: $expected, found: $actual"
    }
}
