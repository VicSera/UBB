package strategy.impl

import entity.Graph
import kotlinx.coroutines.asCoroutineDispatcher
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking
import kotlinx.coroutines.sync.Mutex
import kotlinx.coroutines.sync.withLock
import strategy.HamiltonianCycleFinder
import java.util.*
import java.util.concurrent.Executors

class ParallelHamiltonianCycleFinder(private val nThreads: Int): HamiltonianCycleFinder {
    override fun findInGraph(graph: Graph): List<Int>? {
        var result: List<Int>? = null

        val mutex = Mutex()
        val pool = Executors.newFixedThreadPool(nThreads).asCoroutineDispatcher()

        val stack = Stack<StackElement>()
        stack.push(StackElement(emptyList(), 0))

        while (stack.isNotEmpty() && result == null) {
            val currentElement = stack.pop()
            val currentNode = currentElement.nextNode
            val currentPath = currentElement.path.toMutableList()
            currentPath.add(currentNode)

            runBlocking {
                graph.neighborsOf(currentNode).forEach { nextNode ->
                    launch(pool) {
                        if (nextNode == 0 && currentPath.size == graph.numberOfNodes) {
                            currentPath.add(nextNode)
                            mutex.withLock {
                                result = currentPath
                            }
                        } else if (nextNode !in currentPath)
                            mutex.withLock {
                                stack.push(StackElement(currentPath.toList(), nextNode))
                            }
                    }
                }
            }
        }

        return result
    }

    override fun toString(): String {
        return "Parallel Hamiltonian Cycle Finder"
    }
}
