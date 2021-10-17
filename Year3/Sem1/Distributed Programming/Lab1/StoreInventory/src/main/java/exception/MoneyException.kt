package exception

class MoneyException(
    expected: Float,
    actual: Float
) : CheckStateException("MONEY EXCEPTION: ", null, expected.toString(), actual.toString())
