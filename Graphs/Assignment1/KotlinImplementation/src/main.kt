import graphs.implementations.DirectedGraph
import ui.implementations.Menu

fun main() {
    val graph = DirectedGraph.buildFromFile("graph.txt")
    val ui = Menu(graph)
    ui.launch()
}