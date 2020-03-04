package graphs.implementations

typealias Vertex = Int

class Factory {
    private var currentId = 1

    fun createVertex(): Vertex {
        val vertex = currentId
        ++currentId
        return vertex
    }
}