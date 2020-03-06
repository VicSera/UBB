package graphs.implementations

typealias Vertex = Int

class VertexFactory {
    private var currentId = 1

    fun createVertex(): Vertex {
        val vertex = currentId
        ++currentId
        return vertex
    }
}