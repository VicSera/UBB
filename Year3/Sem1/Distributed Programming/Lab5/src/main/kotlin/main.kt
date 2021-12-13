import strategy.MultiplicationStrategy
import strategy.impl.ParallelOn2Multiplication
import strategy.impl.SequentialKaratsubaMultiplication
import strategy.impl.SequentialOn2Multiplication
import kotlin.system.measureTimeMillis

fun main()
{
    val p1 = Polynomial(mapOf(10 to 2, 5 to 3, 4 to 4, 2 to 2, 1 to 5, 0 to 5))
    val p2 = Polynomial(mapOf(3 to 2, 2 to 7, 1 to 2))
    println("Benchmarking multiplication:\n$p1 *\n$p2")

    benchmark(SequentialOn2Multiplication(), p1, p2)
    benchmark(ParallelOn2Multiplication(), p1, p2)
    benchmark(SequentialKaratsubaMultiplication(), p1, p2)
}

fun benchmark(strategy: MultiplicationStrategy, p1: Polynomial, p2: Polynomial) {
    val millis = measureTimeMillis {
        val result = strategy.multiply(p1, p2)
        println("$strategy: $result")
    }

    println("Strategy $strategy took $millis milliseconds to complete")
}
