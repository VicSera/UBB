package strategy

import entity.Graph

interface HamiltonianCycleFinder {
    fun findInGraph(graph: Graph): List<Int>?
}
