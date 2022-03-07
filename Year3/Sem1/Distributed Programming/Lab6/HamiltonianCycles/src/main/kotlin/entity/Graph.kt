package entity

class Graph(private val adjacencyMatrix: List<List<Boolean>>) {
    val numberOfNodes get() = adjacencyMatrix.size

    fun neighborsOf(node: Int): List<Int> {
        return adjacencyMatrix[node]
            .mapIndexed { index, isPath -> if (isPath && index != node) index else null }
            .filterNotNull()
    }
}
