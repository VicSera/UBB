package ui.implementations

import graphs.interfaces.IGraph
import graphs.interfaces.IMutableGraph

class Menu(
    private val graph: IMutableGraph
): AbstractMenu() {
    override fun launch() {
        val options = listOf(
            "Add vertex", "Add edge", "List vertices", "Get cost", "List inbound edges for a vertex",
            "List outbound edges for a vertex", "Count vertices", "Check edge existence"
        )
        val handlers = listOf(
            ::handleAddVertex, ::handleAddEdge, ::printVertices, ::printCost, ::printInboundEdges,
            ::printOutboundEdges, ::printNumberOfVertices, ::printIsEdge
        )

        while (true) {
            val choice = choose(options)

            handlers[choice]()
        }
    }

    private companion object Parser {
        fun choose(options: List<String>): Int {
            options.forEachIndexed { index, value ->
                println("${index + 1}. $value")
            }

            val userOption = readLine()!!.toInt()
            return userOption - 1
        }
    }

    override fun handleAddEdge() {
        print("Vertex 1: ")
        val vertex1 = readLine()!!.toInt()
        print("Vertex 2: ")
        val vertex2 = readLine()!!.toInt()
        print("Edge cost: ")
        val cost = readLine()!!.toInt()

        graph.addEdge(vertex1, vertex2, cost)
    }

    override fun handleAddVertex() {
        graph.addVertex()
    }

    override fun printCost() {
        // Read two vertices from the stdin and print the cost of the edge between those two vertices if it exists.
        print("Vertex 1: ")
        val vertex1 = readLine()!!.toInt()
        print("Vertex 2: ")
        val vertex2 = readLine()!!.toInt()

        try {
            val cost = graph.getCost(vertex1, vertex2)
            println("The cost of the edge $vertex1 - $vertex2 is $cost")
        }
        catch (excp: NoSuchElementException) {
            println("There is no edge $vertex1 - $vertex2")
        }

    }

    override fun printInboundEdges() {
        print("Which vertex? : ")
        val vertex = readLine()!!.toInt()

        try {
            val iterator = graph.getIncomingEdgeIterator(vertex)
            while (iterator.hasNext()) {
                println("${iterator.next()}")
            }
        }
        catch (excp: NoSuchElementException) {
            println("There is no vertex $vertex")
        }
    }

    override fun printIsEdge() {
        print("Vertex 1: ")
        val vertex1 = readLine()!!.toInt()
        print("Vertex 2: ")
        val vertex2 = readLine()!!.toInt()

        if (graph.isEdge(vertex1, vertex2))
            println("There is an edge!")
        else
            println("The is NO edge!")
    }

    override fun printNumberOfVertices() {
        println("There are ${graph.numberOfVertices} vertices")
    }

    override fun printOutboundEdges() {
        print("Which vertex? : ")
        val vertex = readLine()!!.toInt()

        try {
            val iterator = graph.getOutgoingEdgeIterator(vertex)
            while (iterator.hasNext()) {
                println("${iterator.next()}")
            }
        }
        catch (excp: NoSuchElementException) {
            println("There is no vertex $vertex")
        }
    }

    override fun printVertices() {
        val iterator = graph.getVertexIterator()
        while (iterator.hasNext()) {
            println("${iterator.next()}")
        }
    }
}