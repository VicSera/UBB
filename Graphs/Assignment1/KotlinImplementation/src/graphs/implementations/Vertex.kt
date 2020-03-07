package graphs.implementations

typealias Vertex = Int

class VertexFactory {
    private var currentId = 0

    fun createVertex(): Vertex {
        val vertex = currentId
        ++currentId
        return vertex
    }
}