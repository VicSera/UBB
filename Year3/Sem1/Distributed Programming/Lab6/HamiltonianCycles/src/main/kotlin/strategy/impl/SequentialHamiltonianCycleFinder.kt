package strategy.impl

import entity.Graph
import strategy.HamiltonianCycleFinder
import java.util.*

class SequentialHamiltonianCycleFinder: HamiltonianCycleFinder {
    override fun findInGraph(graph: Graph): List<Int>? {
        val stack = Stack<StackElement>()

        stack.push(StackElement(emptyList(), 0))
        while (stack.isNotEmpty()) {
            val currentElement = stack.pop()
            val currentNode = currentElement.nextNode
            val currentPath = currentElement.path.toMutableList()
            currentPath.add(currentNode)

            graph.neighborsOf(currentNode).forEach { nextNode ->
                if (nextNode == 0 && currentPath.size == graph.numberOfNodes) {
                    currentPath.add(nextNode)
                    return currentPath
                }
                if (nextNode !in currentPath)
                    stack.push(StackElement(currentPath.toList(), nextNode))
            }
        }

        return null
    }

    override fun toString(): String {
        return "Sequential Hamiltonian Cycle Finder"
    }
}
