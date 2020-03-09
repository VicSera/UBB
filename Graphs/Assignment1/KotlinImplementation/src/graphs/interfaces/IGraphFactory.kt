package graphs.interfaces

interface IGraphFactory {
    fun copy(graph: IGraph): IGraph

    fun buildFromFile(fileName: String): IGraph
}