package graphs.interfaces

import graphs.implementations.Vertex

interface IGraph {
    fun isEdge(vertex1: Vertex, vertex2: Vertex): Boolean

    fun getVertexIterator(): IIterator<Vertex>

    fun getOutgoingEdgeIterator(vertex: Vertex): IIterator<Vertex>

    fun getIncomingEdgeIterator(vertex: Vertex): IIterator<Vertex>

    fun inDegree(vertex: Vertex): Int

    fun outDegree(vertex: Vertex): Int

    fun getCost(vertex1: Vertex, vertex2: Vertex): Int
}