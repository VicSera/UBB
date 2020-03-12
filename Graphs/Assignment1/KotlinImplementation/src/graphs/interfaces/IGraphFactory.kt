package graphs.interfaces

interface IGraphFactory {
    fun buildFromFile(fileName: String): IGraph
}