package graphs.interfaces

import graphs.implementations.Vertex

interface IGraph {
    fun addEdge(vertex1: Int, vertex2: Int)

    fun isEdge(vertex1: Int, vertex2: Int): Boolean

    fun getVertexIterator(): IIterator<Vertex>
}