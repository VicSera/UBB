package graphs.implementations

import graphs.interfaces.IGraph
import graphs.interfaces.IIterator
import graphs.interfaces.IMutableGraph

class DirectedGraph(
    _numberOfVertices: Int
) : IMutableGraph {
    var numberOfVertices: Int = _numberOfVertices
        private set
    private val vertices = emptyMap<Int, Vertex>().toMutableMap()
    private val incoming = emptyMap<Int, MutableList<Int>>().toMutableMap()
    private val outgoing = emptyMap<Int, MutableList<Int>>().toMutableMap()

    init {
        for (vertexNumber in 0 until numberOfVertices) {
            vertices[vertexNumber] = Vertex(vertexNumber)
            incoming[vertexNumber] = emptyList<Int>().toMutableList()
            outgoing[vertexNumber] = emptyList<Int>().toMutableList()
        }
    }

    private inner class VertexIterator: IIterator<Vertex> {
        private var currentVertex: Int = 0

        override fun getCurrent(): Vertex {
            return vertices[currentVertex]!!
        }

        override fun isValid(): Boolean {
            return currentVertex in vertices.keys
        }

        override fun next() {
            currentVertex += 1
        }
    }

    override fun
            getVertexIterator(): IIterator<Vertex> {
        return VertexIterator()
    }

    override fun isEdge(vertex1: Int, vertex2: Int): Boolean {
        return vertex2 in incoming[vertex1]!!
    }

    override fun addEdge(vertex1: Int, vertex2: Int) {
        if (isEdge(vertex1, vertex2)) {
            throw Exception("Edge $vertex1-$vertex2 already exists")
        }

        incoming[vertex1]?.add(vertex2)
    }

    override fun addVertex() {
//        val newVertex = Vertex()
    }
}