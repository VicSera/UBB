package graphs.interfaces

interface IIterator<dataType> {
    fun next()

    fun isValid(): Boolean

    fun getCurrent(): dataType
}