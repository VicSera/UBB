package graphs.interfaces

interface IIterator<dataType> {
    fun next(): dataType

    fun hasNext(): Boolean
}