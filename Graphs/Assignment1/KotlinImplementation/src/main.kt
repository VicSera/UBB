import graphs.implementations.DirectedGraph
import ui.implementations.Menu

fun main() {
    val graph = DirectedGraph.buildFromFile("5 6\n0 0 1\n0 1 7\n1 2 2\n2 1 -1\n1 3 8\n2 3 5")
    val ui = Menu(graph)
    ui.launch()
}