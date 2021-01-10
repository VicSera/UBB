package graphs.interfaces

import graphs.implementations.Vertex

interface IMutableGraph: IGraph {
    fun addVertex(vertex: Vertex)

    fun removeVertex(vertex: Vertex)

    fun addEdge(vertex1: Vertex, vertex2: Vertex, vertexCost: Int)

    fun removeEdge(vertex1: Vertex, vertex2: Vertex)
}