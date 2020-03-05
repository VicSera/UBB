package ui.implementations

import graphs.implementations.DirectedGraph

class Menu(
    private val graph: DirectedGraph
): AbstractMenu() {
    override fun launch() {
        while (true) {
            val userInput = readLine()

            println(userInput)
        }
    }

    override fun printCost() {
        // Read two vertices from the stdin and print the cost of the edge between those two vertices if it exists.
        val vertex1 = readLine()!!.toInt()
        val vertex2 = readLine()!!.toInt()

        val cost = graph.getCost(vertex1, vertex2)

        println("The cost of the edge $vertex1 - $vertex2 is $cost")
    }

    override fun printInboundEdges() {
        TODO("not implemented") //To change body of created functions use File | Settings | File Templates.
    }

    override fun printIsEdge() {
        TODO("not implemented") //To change body of created functions use File | Settings | File Templates.
    }

    override fun printNumberOfVertices() {
        TODO("not implemented") //To change body of created functions use File | Settings | File Templates.
    }

    override fun printOutboundEdges() {
        TODO("not implemented") //To change body of created functions use File | Settings | File Templates.
    }

    override fun printVertices() {
        TODO("not implemented") //To change body of created functions use File | Settings | File Templates.
    }
}