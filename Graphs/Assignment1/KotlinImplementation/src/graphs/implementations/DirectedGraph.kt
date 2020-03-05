package graphs.implementations

import graphs.interfaces.IIterator
import graphs.interfaces.IMutableGraph

class DirectedGraph(
    private val factory: Factory,
    _numberOfVertices: Int
) : IMutableGraph {
    val numberOfVertices: Int
        get() = vertices.size
    private val vertices = emptySet<Vertex>().toMutableSet()
    private var inbound = emptyMap<Vertex, MutableSet<Vertex>>().toMutableMap()
    private var outbound = emptyMap<Vertex, MutableSet<Vertex>>().toMutableMap()
    private var cost = emptyMap<Edge, Int>().toMutableMap()

    init {
        for (vertexNumber in 1.._numberOfVertices) {
            val vertex = factory.createVertex()
            vertices.add(vertex)
            inbound[vertex] = emptySet<Vertex>().toMutableSet()
            outbound[vertex] = emptySet<Vertex>().toMutableSet()
        }
    }

    private inner class VertexIterator(vertexSet: MutableSet<Vertex>): IIterator<Vertex> {
        private val setIterator = vertexSet.iterator()
        private var currentVertex = setIterator.next()

        override fun getCurrent(): Vertex {
            return currentVertex
        }

        override fun isValid(): Boolean {
            return setIterator.hasNext()
        }

        override fun next() {
            currentVertex = setIterator.next()
        }
    }

    override fun getVertexIterator(): IIterator<Vertex> {
        return VertexIterator(vertices)
    }

    override fun getIncomingEdgeIterator(vertex: Vertex): IIterator<Vertex> {
        return VertexIterator(inbound[vertex]!!)
    }

    override fun getOutgoingEdgeIterator(vertex: Vertex): IIterator<Vertex> {
        return VertexIterator(outbound[vertex]!!)
    }

    override fun isEdge(vertex1: Vertex, vertex2: Vertex): Boolean {
        return vertex2 in outbound[vertex1]!!
    }

    override fun addEdge(vertex1: Vertex, vertex2: Vertex, vertexCost: Int) {
        if (isEdge(vertex1, vertex2)) {
            throw Exception("Edge $vertex1-$vertex2 already exists")
        }

        outbound[vertex1]?.add(vertex2)
        inbound[vertex2]?.add(vertex1)
        cost[Edge(vertex1, vertex2)] = vertexCost
    }

    override fun removeEdge(vertex1: Vertex, vertex2: Vertex) {
        // Remove cost
        cost.remove(Edge(vertex1, vertex2))

        // Remove vertex2 from vertex1's outbound edges
        outbound[vertex1]!!.remove(vertex2)

        // Remove vertex1 from vertex2's inbound edges
        inbound[vertex2]!!.remove(vertex1)
    }

    override fun addVertex() {
        val newVertex = factory.createVertex()
        vertices.add(newVertex)
    }

    override fun removeVertex(vertex: Vertex) {
        // Remove all costs associated to any edge containing the vertex
        cost = cost.filter {(edge, _) ->
            edge.first != vertex && edge.second != vertex
        }.toMutableMap()

        // Remove all inbound edges
        inbound[vertex]!!.forEach { sourceVertex ->
            outbound[sourceVertex]!!.remove(vertex)
        }
        inbound.remove(vertex)

        // Remove all outbound edges
        outbound[vertex]!!.forEach { destinationVertex ->
            inbound[destinationVertex]!!.remove(vertex)
        }
        outbound.remove(vertex)
    }

    override fun inDegree(vertex: Vertex): Int {
        return inbound[vertex]!!.size
    }

    override fun outDegree(vertex: Vertex): Int {
        return outbound[vertex]!!.size
    }

    override fun getCost(vertex1: Vertex, vertex2: Vertex): Int {
        return cost[Edge(vertex1, vertex2)]!!
    }
}