import entity.Graph
import strategy.HamiltonianCycleFinder
import strategy.impl.ParallelHamiltonianCycleFinder
import strategy.impl.SequentialHamiltonianCycleFinder
import kotlin.system.measureTimeMillis

fun main() {
//    val graph = Graph(listOf(
//        listOf(true, true, false, false, false),
//        listOf(true, true, true, false, false),
//        listOf(false, false, true, true, false),
//        listOf(false, false, false, true, true),
//        listOf(false, true, false, false, true)
//    ))
    val graph = Graph(listOf(
        listOf(true, true, false, false, false),
        listOf(true, true, true, false, false),
        listOf(false, false, true, true, false),
        listOf(false, false, false, true, true),
        listOf(true, false, false, false, true)
    ))


    benchmark(SequentialHamiltonianCycleFinder(), graph)
    benchmark(ParallelHamiltonianCycleFinder(5), graph)
}

fun benchmark(finder: HamiltonianCycleFinder, graph: Graph) {
    val time = measureTimeMillis {
        val result = finder.findInGraph(graph)
        result?.map { "$it" }?.reduce {acc, s -> "$acc -> $s"}?.let {println(it)}
            ?: println("Didn't find a hamiltonian cycle")
    }

    println("$finder took $time milliseconds")
}
